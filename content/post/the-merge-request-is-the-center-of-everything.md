---
title: "The Merge Request Is the Center of Everything"
date: 2026-03-10
draft: false
tags: ["AI", "DevSecOps", "merge requests", "agentic SDLC"]
summary: "IDEs change every 18 months. Agents are disposable. The merge request is the one artifact that survives."
showtoc: true
---

## The convergence nobody planned

Having watched a dozen enterprise teams adopt AI coding agents over the past year, I can tell you the bottleneck has moved. It is no longer writing code. It is reviewing, governing, and shipping the code that agents produce. And the artifact sitting at the center of that bottleneck, the one every tool eventually converges on, is the merge request.

Think about the landscape for a moment. [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [OpenAI Codex](https://openai.com/index/codex/), [Cursor](https://cursor.com/), [Devin](https://devin.ai/), [KiloCode](https://kilocode.ai/), [OpenCode](https://opencode.ai/). Every one of these tools, when it finishes its work, produces the same thing: a proposed change to source code, packaged as a merge request or pull request, submitted for validation and review. Nobody designed this convergence. It happened because the [merge request](https://en.wikipedia.org/wiki/Distributed_version_control#Pull_requests) is the one artifact in the [software development lifecycle](https://en.wikipedia.org/wiki/Software_development_process) where intent, execution, review, governance, and delivery all meet.

You do not need to win the IDE war. IDEs rotate every 18 months, and the current generation of AI-native editors will be no exception. You do not need to win the agent war either, because agents are becoming commoditized faster than anyone predicted. What matters is making the merge request the best possible destination for every change, from every source, validated and governed to enterprise standards.

Not issues. Not epics. Not planning boards. The merge request is where the actual work crystallizes into something reviewable, testable, and deployable. Planning artifacts come and go. The merge request is the moment of truth.

Today's merge request is a diff viewer with a comment thread. Tomorrow's needs to be a workspace.

## The center is hollow

The merge request has not changed in principle since [GitHub](https://github.com/) launched pull requests in 2010. [Scott Chacon](https://scottchacon.com/), GitHub's co-founder, now building [GitButler](https://gitbutler.com/), put it plainly: "The Pull Request has not only hardly changed in principle since we launched it 15 years ago, but worse than that, nobody else has innovated beyond it since."

That was tolerable when humans wrote all the code. It is breaking now, because the volume of proposed changes is climbing while the review surface stays the same size.

The evidence is not anecdotal. [CircleCI](https://circleci.com/) analyzed 28.7 million CI/CD workflows and found something that should worry every engineering leader: feature branch throughput is up 15%, but main branch throughput, the code that actually ships, is down 7%. Teams can write faster. They cannot ship faster. One in seven pull requests now involves an AI agent as author or co-author, and the review process was never built for that volume or that authorship model.

## Five things the merge request is missing

Sitting with customers, running through their agentic workflows, I keep finding the same five gaps. None of them are exotic. All of them are blocking adoption at scale.

**It does not show why.** A reviewer opens an agent-authored merge request and sees a diff. The reasoning, the dead ends, the architectural trade-offs that led to this particular implementation are all gone. The agent session that produced the code is ephemeral, and when it ends, the context dies with it. The reviewer is left to reconstruct intent from output, which is the most expensive kind of code review.

**It does not show what it means.** The merge request has a handful of hardcoded widget types (CI status, test reports, security scans). Customers routinely work around this limitation by faking report types, because the merge request cannot display arbitrary structured data. When your AI agent produces a compliance attestation or a cost-impact analysis alongside the diff, there is nowhere to put it.

**It does not enforce safety for AI-authored code.** When an agent authors a change on behalf of a developer, the requesting developer can still approve their own merge request, because the system treats the AI as the author. This breaks [separation of duties](https://en.wikipedia.org/wiki/Separation_of_duties), and for regulated industries (finance, healthcare, defense), it is a compliance gap that blocks adoption entirely.

**It does not connect to intent.** Specs, architecture decisions, threat models exist somewhere upstream. The merge request has a "closes #123" link and nothing else. For an agent-authored change, the gap between what was requested and what was delivered is wider than it has ever been, and the merge request offers no way to bridge it.

**It does not persist.** Agent sessions are ephemeral by design. When a session ends, the working context evaporates. Another agent, or the same agent in a new session, starts from scratch. The merge request should be a resumable workspace where any actor (human or agent) can pick up where the last one left off. Instead it is a snapshot.

## The competitive landscape is moving

These gaps are not invisible to the market. [Cursor](https://cursor.com/) acquired [Graphite](https://graphite.dev/), merging an AI-native IDE with stacked pull requests and AI code review into a single integrated experience. [GitHub](https://github.com/) is building multi-agent governance with policy-as-code, treating the pull request as an orchestration surface for autonomous agents. [GitButler](https://gitbutler.com/) is rethinking the review unit entirely, moving from branch-based diffs to patch-based review, which is a more natural model when changes come from multiple agents working in parallel.

Nobody has assembled the full vision end to end. The pieces exist across half a dozen products, each solving one or two of the five gaps while leaving the rest open. Whoever stitches together reasoning traces, extensible widgets, AI-aware governance, intent linkage, and persistent workspaces inside the merge request will own the integration point for the entire agentic [SDLC](https://en.wikipedia.org/wiki/Software_development_process). That is the race, and it is happening now, not in some abstract future roadmap.

## What this means if you are adopting AI coding tools today

Having spent the better part of this year helping teams operationalize [agentic workflows](https://en.wikipedia.org/wiki/Software_agent), I keep arriving at the same practical advice. Do not optimize for the agent. Do not optimize for the IDE. Optimize for the merge request, because it is the only artifact that survives when the tooling around it inevitably changes.

Concretely, that means investing in review capacity (humans and automated), not just generation capacity. It means treating your merge request approval policies as governance contracts, not bureaucratic hurdles. It means demanding that every AI tool you adopt can produce a merge request that meets your compliance bar, not just a diff that compiles. And it means evaluating your [DevSecOps](https://en.wikipedia.org/wiki/DevOps#DevSecOps,_shifting_security_left) platform not by how many agents it can spawn, but by how well its merge request experience absorbs the output of agents you have not even adopted yet.

The merge request is already the center of everything. The question is whether we upgrade it to carry the weight, or watch the bottleneck tighten until the productivity gains from AI coding tools show up only on dashboards, never in production.
