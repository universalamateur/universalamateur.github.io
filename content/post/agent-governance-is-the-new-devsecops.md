---
title: "Agent Governance Is the New DevSecOps"
date: 2026-04-12
draft: false
tags: ["AI", "security", "governance", "DevSecOps"]
summary: "I spent weeks building agent governance by hand. Microsoft just open-sourced a toolkit that covers most of it."
showtoc: false
---

I spent weeks building [agent governance by hand](/post/zero-trust-patterns-for-ai-developer-tools/). Container isolation, credential rotation, write gates, network policy, all wired together with [OPA](https://www.openpolicyagent.org/) and shell scripts. It worked. I was proud of it. Then Microsoft open-sourced a toolkit that covers most of it with [less than 0.1 milliseconds of overhead](https://github.com/microsoft/agent-governance-toolkit).

That is a humbling thing to type.

## What Microsoft shipped

The [Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit) (AGT) is a runtime governance SDK. Four execution rings, from unrestricted to fully sandboxed, with per-action policies defined in [YAML](https://en.wikipedia.org/wiki/YAML), [OPA](https://www.openpolicyagent.org/), or [Cedar](https://www.cedarpolicy.com/). A kill-switch that terminates sessions mid-action. An [MCP](https://modelcontextprotocol.io/) Security Scanner that audits tool configurations before the agent starts. Cryptographic agent identity using [Ed25519](https://en.wikipedia.org/wiki/EdDSA#Ed25519) and ML-DSA-65 for post-quantum readiness. SDKs in five languages.

What caught my eye: they score [10/10 on the OWASP Top 10 for Agentic Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/). That is not a marketing claim, it is a coverage map against a published threat model. And the overhead number, <0.1ms per policy evaluation, means there is no performance excuse not to use it.

## They are not alone

Same month. [Ceros](https://www.ceros.com/) shipped guardrails-as-a-service for agent orchestration. [Cycode](https://cycode.com/) launched agent supply chain security, scanning what your agents depend on before they run. [AWS Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) added runtime content filtering for agent outputs. [CircleCI](https://circleci.com/) shipped Chunk, an autonomous CI agent that fixes its own failures.

Four governance products in one month is not a coincidence. It is a category forming in real time.

## What is still missing

AGT solves runtime governance: what an agent CAN do during a session. Per-action policies, execution rings, kill-switch. That is necessary and real.

But nobody is solving the control plane: which agents are allowed where, who authorized them, what tools they can access across an organization, and how you audit all of it after the fact. The gap between "this agent session is governed" and "our organization's agent usage is governed" is where the hard problems live. Identity federation, tool approval workflows, cross-team policy inheritance, audit trails that survive session boundaries.

Runtime governance is the seatbelt. Organizational governance is the traffic system. We have seatbelts now. The roads are still lawless.

## The shift

[DevSecOps](https://en.wikipedia.org/wiki/DevOps#DevSecOps) happened when security stopped being a gate at the end of the pipeline and became infrastructure woven through it. That transition took years, and it started with tooling that made the right thing easier than the wrong thing.

Agent governance is at exactly that inflection point. The tooling just arrived. Runtime governance at <0.1ms overhead and zero cost means there is no rational reason to run an agent without it. The agents are real, the risks are documented, the mitigations now exist as open-source libraries you can install today.

If you are running AI agents in production without a governance layer, you are not being agile. You are being negligent.

I am not retiring my hand-built patterns. Building them taught me what to look for when evaluating a framework. But I am glad the market caught up. The interesting question now is what happens when governance becomes so cheap that not having it is the harder choice to justify.
