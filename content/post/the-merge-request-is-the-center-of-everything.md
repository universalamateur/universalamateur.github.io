---
title: "The Merge Request Is the Center of Everything"
date: 2026-04-09
draft: false
tags: ["AI", "DevSecOps", "merge requests", "agentic SDLC"]
summary: "IDEs change every 18 months. Agents are disposable. The merge request is the one artifact that survives."
showtoc: true
---

## The convergence nobody planned

Having watched a dozen enterprise teams adopt AI coding agents over the past year, I can tell you the bottleneck has moved. It is no longer writing code. It is reviewing, governing, and shipping the code that agents produce. And the artifact sitting at the center of that bottleneck, the one every tool eventually converges on, is the merge request.

Think about the landscape for a moment. [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [OpenAI Codex](https://openai.com/index/codex/), [Cursor](https://cursor.com/), [Devin](https://devin.ai/), [GitHub Copilot](https://github.com/features/copilot), [Augment Code](https://www.augmentcode.com/). Every one of these tools, when it finishes its work, produces the same thing: a proposed change to source code, packaged as a merge request or pull request, submitted for validation and review. Nobody designed this convergence. It happened because the [merge request](https://en.wikipedia.org/wiki/Distributed_version_control#Pull_requests) is the one artifact in the [software development lifecycle](https://en.wikipedia.org/wiki/Software_development_process) where intent, execution, review, governance, and delivery all meet.

You do not need to win the IDE war. IDEs rotate every 18 months, and the current generation of AI-native editors will be no exception. You do not need to win the agent war either, because agents are becoming commoditized faster than anyone predicted. What matters is making the merge request the best possible destination for every change, from every source, validated and governed to enterprise standards.

Today's merge request is a diff viewer with a comment thread. Tomorrow's needs to be a workspace.

## The center is hollow

The merge request has not changed in principle since [GitHub](https://github.com/) launched pull requests in [2008](https://github.blog/news-insights/the-library/drastic-changes/). [Scott Chacon](https://scottchacon.com/), GitHub's co-founder and now CEO of [GitButler](https://gitbutler.com/), put it bluntly: "The Pull Request has not only hardly changed in principle since we launched it 15 years ago, but worse than that, nobody else has innovated beyond it since." [Announcing GitButler's $17M Series A](https://blog.gitbutler.com/series-a) in April 2026, he sharpened the point: organizations are "teaching swarms of agents to use a tool built for sending patches over mailing lists."

That was tolerable when humans wrote all the code. It is breaking now, because the volume of proposed changes is climbing while the review surface stays the same size.

The evidence is not anecdotal. [CircleCI](https://circleci.com/)'s [2026 State of Software Delivery](https://circleci.com/landing-pages/assets/2026-state-of-software-delivery-report.pdf) report found, that among top-performing teams, feature branch throughput surged roughly 50%, while main branch activity, the code that actually ships, stayed flat. [Faros AI](https://www.faros.ai/) confirmed the pattern from a different angle: AI-assisted developers merge 98% more pull requests and interact with 47% more PRs daily, yet organizational delivery metrics remain unchanged. Teams are producing more changes. They are not shipping more software.

And the rejection data tells you where the bottleneck sits. A [Mining Software Repositories 2026](https://conf.researchr.org/home/msr-2026) study found, that 31% of closed agentic pull requests were rejected not for code quality, but for workflow misalignment. The agent produced correct code. The merge request could not carry enough context for the reviewer to understand whether it was the right change.

## Five things the merge request is missing

Sitting with customers, running through their agentic workflows, I keep finding the same five gaps. None of them are exotic. All of them are blocking adoption at scale.

**It does not show why.** A reviewer opens an agent-authored merge request and sees a diff. The reasoning, the dead ends, the architectural trade-offs that led to this particular implementation are all gone. The agent session that produced the code is ephemeral, and when it ends, the context dies with it. The reviewer is left to reconstruct intent from output, which is the most expensive kind of code review.

**It does not show what it means.** The merge request has a handful of hardcoded widget types: CI status, test reports, security scans. When your AI agent produces a compliance attestation or a cost-impact analysis alongside the diff, there is nowhere to put it. Teams routinely work around this limitation by faking report types, because the merge request cannot display arbitrary structured data.

**It does not enforce safety for AI-authored code.** When an agent authors a change on behalf of a developer, the requesting developer can still approve their own merge request, because the system treats the AI as the author. This breaks [separation of duties](https://en.wikipedia.org/wiki/Separation_of_duties), and for regulated industries (finance, healthcare, defense), it is a compliance gap that blocks adoption entirely.

**It does not connect to intent.** Specs, architecture decisions, threat models exist somewhere upstream. The merge request has a "closes #123" link and nothing else. For an agent-authored change, the gap between what was requested and what was delivered is wider than it has ever been, and the merge request offers no way to bridge it.

**It does not persist.** Agent sessions are ephemeral by design. When a session ends, the working context evaporates. Another agent, or the same agent in a new session, starts from scratch. The merge request should be a resumable workspace where any actor, human or agent, can pick up where the last one left off. Instead it is a snapshot.

## The competitive landscape confirms it

These five gaps have not gone unnoticed, and what I find telling is, that every company attacking the problem ends up at the same place: the merge request.

[GitHub](https://github.com/) opened [Agent HQ](https://github.blog/news-insights/company-news/welcome-home-agents/) to public preview, where [Copilot](https://github.com/features/copilot), [Claude](https://www.anthropic.com/claude), and [Codex](https://openai.com/index/codex/) agents run inside the platform with session status visible in issues and pull requests. [Cursor](https://cursor.com/) acquired [Graphite](https://graphite.dev/) in [December 2025](https://techcrunch.com/2025/12/19/cursor-continues-acquisition-spree-with-graphite-deal/), merging an AI-native IDE with stacked pull requests and AI code review into one vertically integrated loop. [Graphite's code review](https://graphite.dev/features/code-review) has an unhelpful-comment rate under 3%, and developers change their code 55% of the time when the AI flags an issue. [GitButler](https://gitbutler.com/), freshly funded, is rethinking the review unit entirely, moving from branch-based diffs to [patch-based review](https://blog.gitbutler.com/butler-review/) with commits as the reviewable unit, a model that makes more sense when three agents touched the same branch.

Even the tools that market themselves as autonomous end up at the same bottleneck. [Augment Code](https://www.augmentcode.com/) reported, that their three-agent orchestration dropped average time-to-merge from three days to just over one day at [Tekion](https://tekion.com/). [Devin](https://devin.ai/) Review catches roughly 30% more issues than unreviewed PRs. The "autonomous software engineer" still submits a pull request and waits for a human to approve it.

Nobody has assembled the full picture. The pieces exist across half a dozen products, each solving one or two of the five gaps. I keep waiting for someone to stitch together reasoning traces, extensible data layers, governance for AI-authored code, intent linkage, and persistent workspaces inside the merge request. That combination is the race, and it is happening now.

## What comes next

I do not know the exact sequence, but watching these pieces fall into place, I can see the general shape.

The merge request gains context first, because it is the cheapest thing to build. Agent reasoning traces show up as reviewable [CI artifacts](https://en.wikipedia.org/wiki/Artifact_(software_development)) alongside the diff. Specs link bidirectionally to their implementing changes. The review experience starts to differentiate between human-authored and agent-authored code, not to restrict, but to inform. Some teams are shipping this already.

After that, the merge request becomes a workspace. Sessions persist across actors. An agent starts a change, a human refines it, another agent adds tests, a reviewer requests modifications, and the entire history is navigable. [Stacked](https://graphite.dev/guides/stacked-prs) and chained merge requests enable parallel agent work on interdependent changes. The merge request stops being a submission surface and becomes a collaboration surface.

What happens further out is harder to predict. I suspect the discrete "request" model eventually gives way to [continuous delivery](https://en.wikipedia.org/wiki/Continuous_delivery) streams, where changes flow through governance checkpoints without anyone clicking a merge button. The diff is still there, but it becomes one view among many, alongside intent graphs, cost projections, and [compliance attestations](https://en.wikipedia.org/wiki/Software_supply_chain). Whether that takes three years or ten, I genuinely do not know.

## What this means if you are adopting AI coding tools today

Having spent the better part of this year helping teams operationalize [agentic workflows](https://en.wikipedia.org/wiki/Software_agent), I keep arriving at the same practical advice. Do not optimize for the agent. Do not optimize for the IDE. Optimize for the merge request, because it is the only artifact that survives when the tooling around it inevitably changes.

Concretely, that means investing in review capacity (humans and automated), not just generation capacity. It means treating your merge request approval policies as governance contracts, not bureaucratic hurdles. It means demanding, that every AI tool you adopt can produce a merge request that meets your compliance bar, not just a diff that compiles. And it means evaluating your [DevSecOps](https://en.wikipedia.org/wiki/DevOps#DevSecOps,_shifting_security_left) platform not by how many agents it can spawn, but by how well its merge request experience absorbs the output of agents you have not even adopted yet.

The merge request is already the center of everything. The question is whether we upgrade it to carry the weight, or watch the bottleneck tighten until the productivity gains from AI coding tools show up only on dashboards, never in production.
