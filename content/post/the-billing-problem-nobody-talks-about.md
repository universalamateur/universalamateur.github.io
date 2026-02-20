---
title: "The Billing Problem Nobody Talks About"
date: 2026-02-20
draft: false
tags: ["AI", "billing", "DevSecOps", "enterprise"]
summary: "Every enterprise adopting AI coding tools hits the same wall within 90 days: nobody knows what it costs."
showtoc: true
---

Having the same conversation for the fourth time in a month, with a different enterprise customer each time, I have accepted that this is now a pattern and not a coincidence. The conversation goes like this: an engineering organization adopts an AI coding tool ([GitHub Copilot](https://github.com/features/copilot), [Cursor](https://cursor.com/), [Claude Code](https://docs.anthropic.com/en/docs/claude-code), pick your favorite), celebrates a quarter of productivity gains, and then someone from finance walks into a room and asks a question that nobody can answer. "What are we spending on this?"

The excitement phase is real. Developers are faster. Pull requests move quicker. [DORA metrics](https://dora.dev/) improve. I do not dispute any of that. What I dispute is the assumption, that the billing and cost governance will sort itself out. It will not. It never does. And the gap between "this tool is great" and "we know what it costs per team per quarter" is where I keep finding organizations stuck, usually around the 90-day mark.

## Three tiers of billing maturity

I found early in my conversations, that the maturity of an organization's AI billing posture falls into one of three tiers, each with its own failure mode.

### Tier 1: Included credits (the trap)

Credits bundled with the subscription. The most dangerous of the three, precisely because it feels free. Nobody tracks consumption because there is no line item to track. The monthly invoice looks the same whether 50 developers are using the tool or 500.

Then one quarter, usage spikes 400% because someone enabled agentic workflows and the agents are burning tokens at a rate no human developer could match. The CTO discovers that the "included" credits ran out two months ago and overage charges have been accruing silently. Zero visibility breeds zero governance. If you cannot see the meter, you cannot manage the spend. The trap is not that included credits are expensive. The trap is that they are invisible.

### Tier 2: On-demand usage (the panic)

Pay-per-use with no commitment. Full visibility into spend, which sounds like progress until you realize it comes with zero predictability. Finance cannot forecast quarterly costs because consumption fluctuates with sprint intensity, team headcount changes, and whether someone left an agent running over the weekend.

Every sprint review becomes a budget conversation. Engineering managers start self-throttling AI usage to stay within informal limits that nobody formally set, which defeats the entire purpose of adopting AI tools in the first place. The organization bought acceleration and then applied the brakes because the financial governance was not there to absorb variable spend.

This is the phase where I see the most organizational friction, because the people who see the bill (finance) and the people who generate the bill (engineering) have no shared framework for resolving the tension.

### Tier 3: Pre-commitment with consumption tracking (the goal)

Committed credit pools, analogous to [reserved instances](https://en.wikipedia.org/wiki/Amazon_Elastic_Compute_Cloud#Reserved_instances) in cloud infrastructure, provide the revenue floor that finance needs for forecasting. Consumption tracking layered on top provides the per-team, per-project, per-workflow visibility that engineering leadership needs for accountability. Spend caps and alerts provide the governance rails, that prevent any single team or runaway agent from consuming the entire pool.

[Snowflake](https://www.snowflake.com/) proved this model works at scale, sustaining 127% net revenue retention with a consumption-based pricing model that enterprises learned to budget around. [AWS Bedrock](https://aws.amazon.com/bedrock/) is moving agent infrastructure in the same direction. The pattern is established. What is missing in most enterprises is the internal machinery to operate within it.

This is where every organization needs to get to. Almost none are there today.

## The governance gap that arrives before the security gap

Here is what surprises people: the billing governance gap catches leadership off guard before the security gap does. Not because security does not matter (it does, enormously), but because security gets budget, attention, a dedicated team, and executive sponsorship from day one. Cost attribution gets a spreadsheet.

When 500 engineers start burning tokens with no cost attribution per team, the financial governance gap surfaces within weeks. "Who sees the bill?" is the simplest governance question an organization can ask about its AI tooling, and it is consistently the one engineering leadership can least answer, because the billing infrastructure was designed for seat-based licensing and nobody rebuilt it for consumption-based pricing.

The shift from seat-based to consumption-based pricing is happening across the entire DevSecOps industry, and the number of consumption-based SKUs is proliferating faster than billing infrastructure can support them. Code completion, chat, agentic workflows, autonomous agents, each carries its own token economics. Organizations whose internal financial governance assumes a per-seat world are the ones getting caught.

## Self-managed environments have it worse

For organizations running self-managed or air-gapped deployments, the billing visibility problem compounds. There is no cloud-side metering automatically tracking consumption. Billing depends on periodic usage reports, persistent telemetry channels, or manual aggregation. The data needed for cost attribution either arrives late, arrives incomplete, or does not arrive at all.

[SOX compliance](https://en.wikipedia.org/wiki/Sarbanes%E2%80%93Oxley_Act) requirements add another layer, that most teams underestimate. Any revenue-touching billing system, which consumption-based AI pricing absolutely is, must meet audit and control standards that a spreadsheet-based process cannot satisfy. The gap between "we track this in a sheet" and "this is SOX-compliant" is measured in months of work and significant tooling investment.

## What to do about it

The [FinOps](https://www.finops.org/) discipline, born from cloud infrastructure cost management, is the closest existing framework. The core principle transfers directly: make cost visible, allocate it to the teams that generate it, create feedback loops so that engineering decisions carry financial context. FinOps practices for cloud spend optimization are the starting point, not the destination, for AI tool cost governance.

Before you adopt the next AI coding tool, ask your team one question: "Who sees the bill?" If they cannot answer in 30 seconds, you have found something to fix. Not next quarter. Not when finance asks. Now, while the spend is still small enough to govern and before the agentic workflows turn the consumption curve into something nobody budgeted for.
