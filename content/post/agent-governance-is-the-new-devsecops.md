---
title: "Agent Governance Is the New DevSecOps"
date: 2026-04-12
draft: false
tags: ["AI", "security", "governance", "DevSecOps"]
summary: "I spent weeks building agent governance by hand. Then Microsoft open-sourced a toolkit that covers most of it."
showtoc: false
---

I spent the better part of a month building agent governance from scratch. Container isolation with read-only root filesystems and dropped [Linux capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html). Self-rotating credentials with 15-minute TTLs. Write gates that require human approval for every external mutation. [Policy-as-code](https://www.openpolicyagent.org/) evaluated at runtime, not documented on a wiki page. Six patterns, tested across financial services, automotive, and defense. I wrote about them [in detail](/post/zero-trust-patterns-for-ai-developer-tools/), and I was proud of the result.

Then [Microsoft](https://www.microsoft.com/) released the [Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit).

## What caught my eye

AGT is an open-source runtime governance SDK. Four execution rings, from Privileged down to Sandboxed, with per-action policies written in YAML, [OPA](https://www.openpolicyagent.org/), or [Cedar](https://www.cedarpolicy.com/). A kill-switch for immediate agent termination. An [MCP](https://modelcontextprotocol.io/) Security Scanner that audits tool configurations before the agent starts. [Zero-trust](https://en.wikipedia.org/wiki/Zero_trust_security_model) agent identity using [Ed25519](https://en.wikipedia.org/wiki/EdDSA) plus post-quantum [ML-DSA-65](https://en.wikipedia.org/wiki/CRYSTALS-Dilithium). SDKs in five languages. Coverage of the [OWASP Agentic](https://owasp.org/www-project-top-10-for-large-language-model-applications/) security risks.

Policy evaluation overhead: less than 0.1 milliseconds.

Where I had to wire up [Podman](https://podman.io/) rootless containers, tmpfs mounts, and custom entrypoint scripts, AGT declares execution rings in a configuration file. Where I wrote OPA policies for each credential tier, AGT ships policy templates that cover the common patterns. I built governance by hand. Microsoft made it a `pip install`.

## They are not alone

AGT is the most complete implementation I have seen, but it is not an outlier. [AWS Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) applies runtime content filtering and grounding checks to model invocations. [CircleCI](https://circleci.com/) shipped an autonomous CI agent that diagnoses build failures and opens pull requests automatically. [Cursor](https://cursor.com/) built event-driven automations where AI-generated fixes are proposed as pull requests, with over a third merged directly. Startups are building guardrails-as-a-service and agent supply chain security.

Multiple governance products appearing in the same month is not a coincidence. It is a category forming.

## What is still missing

Here is what I noticed comparing AGT to what I built. AGT handles the runtime: what an agent can do in the moment. Per-action policies, execution rings, kill-switch. All essential.

Nobody handles the control plane.

Which agents are allowed in which environments? Who approved this agent's access to production credentials? When did the policy last change, and who reviewed it? How do you audit across fifty teams running different agents with different governance configurations?

Picture an enterprise with five AI coding agents across twenty teams. Each team configured its own policies. Some have kill-switches. Some do not. Nobody has a single view of what is running, what it can access, or whether the governance is current. That is the gap, and it is the gap that matters for regulated industries.

The distance between "this agent's actions are governed" and "this organization's agent usage is governed" is where the real work remains.

## The parallel

[DevSecOps](https://en.wikipedia.org/wiki/DevOps#DevSecOps) happened when security stopped being a gate at the end of the pipeline and became infrastructure woven into every stage. Automated scanning in CI. Policy enforcement in merge requests. Compliance as code, not compliance as audit. The early adopters looked paranoid. Then breaches happened, regulations tightened, and the paranoid teams were the only ones still shipping.

Agent governance is at exactly that inflection point. The tooling exists. The overhead is negligible. The standards are published. If you are running AI agents in production without a governance layer, you are not being agile. You are being negligent.

## What I am doing about it

I am not retiring my hand-built patterns. They work, and I understand every line. But I am evaluating AGT seriously, because governance that costs nothing to add and less than a millisecond to run removes every excuse.

The question is no longer whether agent governance will become standard. It will. The question is what happens when governance is so cheap that not having it becomes the harder position to defend.
