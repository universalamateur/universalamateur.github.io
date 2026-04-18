---
title: "The Dark Factory Is Not Unstaffed"
date: 2026-04-18
draft: false
tags: ["AI", "agentic engineering", "engineering culture", "merge requests"]
summary: "Notes from the floor of a factory that is still being built."
showtoc: false
---

You have heard the phrase. [Dark factory](https://en.wikipedia.org/wiki/Lights_out_(manufacturing)). Lights-out manufacturing. No humans on the floor, because the robots do not need to see. The software industry is building the same thing. Business intent goes in at one end. Value-delivering software comes out the other. In between, agent teams do the work, Context Engineers and Harness Engineers maintain the plumbing, product overseers supervise outcomes, and business analysts collect intent. This is not a prediction. It is being built right now, in the companies I spent this week talking to.

## The floor we are on

I spent my PTO this week talking to Staff+ engineers, tech leads, and engineering managers across my field. Every one of them is exhausted. I include myself in the sample.

The role has shifted for all of them. Code author to orchestrator. Diagram architect to spec designer and product manager for agents. Every one of them has multiple agent sessions open at the same time. Mobiles tethered to their agent teams, so they can poke them at 11pm. Long nights. Weekends that were not supposed to be working weekends. Throughput has never been higher. Rest has never been rarer.

We are currently the factory floor of the factory we are building.

## Why the senior IC is the load-bearing beam

The last 20% is still human. The hardcore manual testing, the edge-case hunting, the acceptance-test intuition that comes from years of POCs and production incidents. Knowing where the agent quietly went wrong. Knowing which niche to poke that the spec did not anticipate.

Every senior engineer I spoke to said the same thing I have been saying to myself all year: if I had done the AI engineering without that experience, without seeing where the agents went wrong or testing the niches that only come from years of acceptance-testing and POC experience, most of my projects this year would have failed.

The emerging shorthand is a flip from 80/20 to 20/80. The model does 80%. The human does 20%. But that 20% is the part that needs the most experience, not the least. It cannot be delegated to juniors, because juniors do not yet have the pattern-match for what looks right but is not.

Before agents, the senior engineer was the person who wrote the hardest parts. Now the senior engineer is the person who catches what the agent got wrong in the hardest parts. Same person, different fulcrum. Both roles burn your experience at the same rate.

This is why the exhaustion concentrates at Staff+. It is not an accident. It is a diagnostic signal.

## The review layer has already collapsed

There is a quieter finding from the week, and it is the one that keeps me up.

Nobody likes reviewing anymore.

The merge requests are bigger. The changes are bigger. The reviewer opens the diff, does a surface glance, checks that the pipeline is green, and approves. Not AI slop. Just massive, correct-looking changes landing faster than any human can comprehend them.

The data agrees with what my peers told me. [Faros AI](https://www.faros.ai/) measured that AI-assisted developers merge 98% more pull requests and interact with 47% more PRs daily. [CircleCI](https://circleci.com/)'s [2026 State of Software Delivery](https://circleci.com/landing-pages/assets/2026-state-of-software-delivery-report.pdf) found feature-branch throughput up roughly 50% on top-performing teams, while main-branch activity stayed flat. [Mining Software Repositories 2026](https://conf.researchr.org/home/msr-2026) found that 31% of closed agentic pull requests were rejected not for code quality, but for workflow misalignment. The agent produced correct code. The reviewer could not carry enough context to tell whether it was the right code.

Here is the shape of the collapse. The reviewer does not have the context to evaluate a change this large. The reviewer does not have the time to slow down and build the context. The reviewer is also the author on two other merge requests, waiting on their own review. The green pipeline is the only signal the reviewer can process at the speed the work is moving. So the green pipeline becomes the approval gate, with the human approval as a formality on top.

This is not laziness. It is what load-shedding looks like under pressure. The review ritual is still happening. The review function is not. That is the crack.

## What good managers are already doing

The good managers saw this before I did.

Talk to a tech lead or an engineering manager whose team has been running agents in production for six months and you will hear the same story. Teams exhausted. Review queue stretching. Changes merging but not deploying, or pushing to main against policy, or auto-merging on green after a pipeline-and-test refactoring sprint that finally made the pipeline load-bearing.

That last pattern is the one that works. Replace the human review step with the pipeline itself. Make the tests the gate. Make the security scan the gate. Make the policy checks the gate. When the pipeline is actually doing the work that a distracted reviewer used to pretend to do, auto-merge on green stops being reckless and starts being honest.

This is the current frontier of engineering management, and it is happening quietly, project by project, without anyone naming it yet. The managers doing it well are the ones whose teams are starting to recover. The managers not doing it are the ones whose review queues are visibly growing.

## The loop

Here is what I think is actually happening underneath the exhaustion.

Model capability expands. Leadership reprices the goalposts, because the new tools make the old estimates look conservative. The senior IC absorbs the new work, which is the last 20% of every project plus the orchestration of agents plus the spec design plus the quality judgment plus whatever review capacity can be scraped together. Merge-request volume rises. Review comprehension collapses, because no human can keep up. Good managers re-plumb the pipeline so the tests become the gate. Managers who do not re-plumb watch the queue balloon. Either way, the senior IC keeps burning, because every round of model capability raises the ceiling the IC is now expected to reach.

This is the loop. It is why the exhaustion is universal among the people I spoke to, not isolated.

This pattern looks like [Jevons paradox](https://en.wikipedia.org/wiki/Jevons_paradox) applied to cognitive labor. Tasks got faster, so expectations rose, so the workload expanded to fill the capacity gain. [DORA 2025](https://dora.dev/) reports aggregate burnout roughly flat across the industry. The aggregate is misleading. The distribution is uneven, and Staff+ is where it is concentrated.

## What the next two years probably look like

I can see the next two years clearly enough.

The orchestrator role holds, with better tooling for research, problem decomposition, and review assist. Spec design plus test-driven development becomes a named discipline, taught and hired for. Intent articulation and business-outcome definition get pulled into the engineering role, because that is where the translation loss between leadership and agent teams actually happens. Observability of agent work becomes table stakes. Context Engineering and Harness Engineering become real titles on real job ladders.

I am not strong enough to believe what will be in five years.

What I am sure of is that the roles are not yet clearly defined, including the one I hold right now, and pretending otherwise is how you make the exhaustion worse. Everyone I spoke to agreed on at least this: the people who are surviving best are the ones who have stopped pretending they know the shape of the destination.

## Where I am standing

Here is where I am personally standing, for what it is worth.

I have chosen escape velocity through mastery. Not escape from the field, not managing sideways into something quieter, not waiting for the model curve to flatten. I work for a company that builds the tools and the plumbing for this shift, and my bet is to go deeper into that role, not sideways out of it.

That means using my competitors' tools, regularly, so I can walk in my customers' shoes. It means staying on the bleeding edge of the projects that feel most uncertain, because uncertainty is where the learning is. It means staying in conversation with peers, because nobody has this figured out, and the people who pretend they do are the ones I trust the least.

I want to listen to my peers. I want to have the hard conversations with them about how they see the future, and what they are doing with it. This blog post is one of those conversations.

## The close

The factory is being built. We are the floor. That is a real place to be standing, and it is worth saying out loud.

Is this just my bubble, or is it yours too?

If you are Staff+ or leading a team in software right now, I want to hear what you are seeing.
