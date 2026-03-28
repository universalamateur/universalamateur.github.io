---
title: "What I Learned Speaking About AI at an Automotive Conference"
date: 2026-03-28
draft: false
tags: ["AI", "automotive", "speaking", "conferences"]
summary: "What happens when you present AI governance to 300 automotive executives on a Friday afternoon in Ingolstadt."
showtoc: false
---

Standing in the [Maritim Hotel](https://www.maritim.com/en/hotels/germany/hotel-ingolstadt) in [Ingolstadt](https://en.wikipedia.org/wiki/Ingolstadt) on a Friday around noon, with 300 automotive executives settling into the post-lunch energy dip, I had exactly 15 minutes to make a point about AI governance. The [Car IT Symposium](https://www.carit-symposium.de/) is one of those events where the German automotive industry sends its engineering leadership to hear about technology trends, and my silver sponsor slot fell right into the window where coffee is wearing off and lunch is pulling people toward their chairs with gravitational certainty.

The talk was titled "Your Models, Your Rules: Who Really Controls AI in Your Engineering Process?" which, for a 15-minute slot, is already doing a lot of heavy lifting in the title alone.

## The Bridge That Wrote Itself

What made the slot work was timing I could not have planned. The talk immediately before mine was from [Synopsys](https://www.synopsys.com/), presenting their AI-powered code scanning capabilities, showing the audience what modern static analysis can find in automotive codebases. Walking up to the lectern with that context still fresh in the room, I opened with a single reframing: "The talk you just saw showed you what AI can find in your code. I am here to ask: who controls what happens next?"

That bridge, from detection to governance, landed better than anything else I said that day. The room shifted. You could see it in the body language, the way people who had been leaning back after a solid Synopsys demo suddenly sat forward, because the question implied that finding problems is only half the story.

## Three Questions for Monday Morning

Rather than walking through architecture diagrams or product demos, I structured the entire talk around three questions that every automotive engineering leader should be asking their teams.

**Who controls the model?** Can you swap [Claude](https://www.anthropic.com/claude) for [Mistral](https://mistral.ai/) tomorrow if your compliance team requires it? Can you move from a cloud provider to on-prem with [Ollama](https://ollama.com/) when a customer's data residency requirements change? If the answer is "not without six months of re-integration," you have a vendor lock-in problem disguised as an AI strategy.

**Who sets the rules?** Where are the guardrails defined, who can change them, and are they auditable? In an industry that lives by [ASPICE](https://en.wikipedia.org/wiki/Automotive_SPICE) process assessments and [ISO 26262](https://en.wikipedia.org/wiki/ISO_26262) functional safety standards, "the AI team configured it" is not an acceptable answer to an auditor.

**Who sees the bill?** What happens when 500 engineers across your organization start burning tokens with no visibility into consumption, no cost attribution per team, and no way to correlate spend with output? The financial governance gap in enterprise AI adoption is, in my experience, consistently the one that catches leadership off guard first.

## Why It Resonated

The automotive world is not [Silicon Valley](https://en.wikipedia.org/wiki/Silicon_Valley). These are people who write software that goes into vehicles carrying human lives, governed by [MISRA C](https://en.wikipedia.org/wiki/MISRA_C) coding standards and functional safety processes that predate the current AI wave by decades. Their supply chains span 40 or more tier-1 suppliers, each with their own toolchains, their own compliance requirements, their own interpretation of what "secure" means. And with the [EU AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act) enforcement coming in August 2026, regulatory pressure on AI governance is not theoretical for this audience. It is a line item on their project plans.

The "governance first" framing resonated precisely because these people already think in governance terms. They do not need to be convinced that oversight matters. What they needed, and what I think the talk delivered, was a simple vocabulary for the specific oversight gaps that AI introduces into their existing processes.

The gap between Silicon Valley AI enthusiasm and German industrial reality was visible in the room. Several hallway conversations afterward circled around the same theme: "We know we need AI. We do not know how to govern it within the frameworks we already have."

## What Travels

Looking back, the thing that worked was not the content itself but the format. Three questions, each expressible in a single sentence, each pointing at a governance gap that is easy to verify ("go ask your team, and if they cannot answer in 30 seconds, you have found something to fix"). The framework is simple enough to repeat in a hallway, memorable enough to survive the drive back to Munich or Stuttgart, and actionable enough that a CTO hearing it secondhand on Monday morning can do something with it.

That was the goal: give 300 executives something they would say to their CTO the following week. "Have you asked the three questions?" If even a handful of those conversations happened, the 15 minutes were worth it.
