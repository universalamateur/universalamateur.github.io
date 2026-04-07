---
title: "Zero-Trust Patterns for AI Developer Tools"
date: 2026-04-07
draft: false
tags: ["AI", "security", "zero trust", "DevSecOps"]
summary: "Six patterns for running AI coding agents in environments where the container is assumed compromised."
showtoc: true
---

Helping regulated enterprises adopt AI coding agents, I keep encountering the same architectural contradiction: the agent needs access to source code, cloud APIs, and developer infrastructure to be useful, but the agent itself runs untrusted code. [Simon Willison](https://simonwillison.net/) and [Martin Fowler](https://martinfowler.com/) have described this as the "lethal trifecta" of AI security risk: access to sensitive data, exposure to untrusted content, and the ability to communicate externally. Any two of the three are manageable. All three together require a fundamentally different security posture.

The answer, I found early in my work with containerized agent runtimes, is not to trust the agent less but to architect the runtime so that trust is irrelevant. [Zero trust](https://en.wikipedia.org/wiki/Zero_trust_security_model) applied to AI developer tools means the container, the credentials, the network, and the write path are all designed to function correctly even when the agent inside them is actively compromised. Here are six patterns I have built and tested across financial services, automotive, and defense. None require exotic tooling.

## Container isolation as the default

The container that runs the agent is assumed compromised from the moment it starts. This is not pessimism, it is a design constraint that simplifies everything downstream.

In practice this means a read-only root filesystem, [tmpfs](https://en.wikipedia.org/wiki/Tmpfs) mounts for working data that vanish when the session ends, all [Linux capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html) dropped, and an unprivileged user with no escalation path. [Podman](https://podman.io/) rootless containers make this straightforward without a daemon running as root. For higher-isolation environments, [Firecracker](https://firecracker-microvm.github.io/) microVMs provide a hardware-level boundary, that an attacker who escapes the container still lands inside a minimal VM with no host access.

If an attacker gains shell inside the agent's runtime, what do they get? Read-only filesystem, short-lived tokens, no network access to anything not explicitly allowed, no persistent storage. A box designed to be thrown away, and they get thrown away with it.

## Task-scoped credentials, never shared

Persistent credential stores inside agent runtimes are the single most dangerous pattern I see in enterprise AI deployments. A long-lived API token in an environment variable inside a container processing untrusted input is an invitation written in neon.

The pattern I have settled on uses three tiers. Self-rotating tokens, where minting a new token immediately invalidates the old one, so a stolen credential is dead by the time an attacker tries it. Certificate-minted tokens using [JWT](https://en.wikipedia.org/wiki/JSON_Web_Token) bearer flows with a 15-minute TTL, where the signing certificate lives in [HashiCorp Vault](https://www.vaultproject.io/) (or [OpenBao](https://openbao.org/) for the open-source path) and the agent never sees the private key. And mint-and-expire tokens with a 60-minute TTL for lower-sensitivity operations, expiring naturally, never refreshed.

[SPIFFE](https://spiffe.io/) workload identity gives each session a cryptographically verifiable identity without embedding secrets. The runtime proves who it is by workload attestation, not by presenting a credential that could be copied. No tier stores credentials on disk. No tier shares tokens between sessions.

## Human-in-the-loop write gates

All external writes, every [CRM](https://en.wikipedia.org/wiki/Customer_relationship_management) update, every Slack message, every Git commit, every cloud resource modification, require explicit human confirmation. The agent drafts, the human approves. This is not a UX convenience pattern. It is a security boundary.

Having watched an unconfigured agent send an internal project identifier to a customer-facing Slack channel (an incident I described in an [earlier post](/post/configuring-ai-agents-that-dont-embarrass-you/)), I am not theoretical about this. The write gate intercepts the action, presents a dry-run table (target system, proposed change, data involved), then waits for a human to say yes.

Read operations and write operations belong to fundamentally different trust categories. Reading a file, querying an API, searching a codebase, these are safe to auto-execute. Anything that changes state in a system visible to other humans crosses a boundary, that boundary needs a gate, and that gate needs a person.

## Default-deny networking

Outbound network access from the agent runtime is denied by default. Every allowed destination is declared explicitly in a policy file: hostname allowlists, port restrictions, protocol constraints. DNS resolution happens through a policy proxy, not inside the sandbox, so the agent cannot resolve hostnames the policy has not approved.

This inverts the typical container networking model, where outbound is open and you block the bad destinations after the fact. Default-deny means the agent reaches exactly the APIs and services its task requires, nothing else. No path to the public internet, no path to internal services it does not need.

Egress logging captures every connection attempt, successful or denied. When the [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) lists prompt injection as a top risk, default-deny networking is the infrastructure-level answer, that even a successfully injected prompt cannot exfiltrate data to a destination the policy has not blessed.

## Policy-as-code, not honor system

Every pattern described above, the container configuration, the credential scopes, the network allowlists, the write gate rules, exists as a version-controlled configuration file. Not as a wiki page, not as a comment in an agent prompt, not as tribal knowledge held by the platform team.

[Open Policy Agent](https://www.openpolicyagent.org/) (OPA) evaluates these policies at runtime, making enforcement programmatic rather than procedural. Data classification rules, credential scope definitions, network policies, all living in the same repository as the infrastructure code, reviewed through the same merge request process, subject to the same approval gates.

Auditors do not accept "we told the agent not to do that" as evidence of a control. [SOC 2](https://en.wikipedia.org/wiki/System_and_Organization_Controls) and [ISO 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001) audits require demonstrable, reviewable, versioned controls. Policy-as-code turns security configuration into something an auditor can diff against the previous version and verify was reviewed by a human before deployment.

## Audit trails that survive the session

When the agent session ends and the container is destroyed (and it should be destroyed, not recycled), the audit record must persist. Every tool invocation, every credential mint, every write gate decision, every network connection attempt, logged to a store that outlives the ephemeral runtime.

This is the pattern, that I found most often missing in early deployments. The container is properly isolated, the credentials properly scoped, but when a compliance team asks "what did the agent do last Thursday," the answer is silence, because the logs went away with the container.

Structured audit events shipped to an immutable log store before the session ends give regulators what they need: evidence, not trust. The trail captures what the agent did, what it was allowed to do (the policy snapshot), what was denied, and what credentials it held.

## These patterns are not aspirational

Everything described here runs on standard tooling. [Podman](https://podman.io/) for rootless containers. [OPA](https://www.openpolicyagent.org/) for policy evaluation. [Vault](https://www.vaultproject.io/) or [OpenBao](https://openbao.org/) for secret brokering. [SPIFFE](https://spiffe.io/) for workload identity. Standard log shipping to whatever immutable store your compliance team already trusts.

The instinct in regulated environments is to either lock down everything (making the agent useless) or grant broad access and hope the model behaves (making the agent dangerous). Zero trust applied to agent runtimes offers a third path: grant precisely the access the task requires, enforce it at the infrastructure level, make every decision auditable, and destroy the runtime when the work is done.

I have watched enough enterprise AI pilots stall on security review to know, that the blocker is rarely the technology. It is the absence of a legible security architecture, that compliance teams can evaluate. Six patterns, each implementable in a week, each auditable, each explainable to a CISO in a single sentence. That is the difference between a pilot that passes security review and one that dies in committee.
