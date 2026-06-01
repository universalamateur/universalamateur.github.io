---
title: "Renting Your Own Accountability"
date: 2026-05-31
draft: false
tags: ["AI", "agents", "platform engineering", "AgentOps", "governance", "Applied AI Engineering"]
summary: "A follow-up to The Manager of Agents. I named three roles and missed a fourth: the platform tier that builds and runs the harness. It is also the one place the enterprise is quietly renting its own accountability."
showtoc: true
---

I published a bet, and then I found the hole in it.

[The Manager of Agents](./post/the-manager-of-agents/) argued that the unit of work in software is moving from a human writing code to a fleet of agents writing it, and it named three roles for the people who remain. The AI Engineer builds the substrate. The Applied AI Engineer, or Manager of Agents, directs a fleet and owns what it ships. The AI-assisted Software Engineer still types, with the agent as a copilot. My bet was that the middle role is durable and the third is being absorbed into it.

I missed a role. It sits at a different table from the three I drew, and it is the one that decides whether the bet survives contact with the enterprise.
## The question my taxonomy could not answer
The gap showed up as a plain question. Take the most boring durable role in modern software: the DevOps engineer who runs CI/CD for several teams. A workhorse that has not gone anywhere. What is its agentic-age analog?

Run it against my three roles and none of them fit. The DevOps-for-many-teams engineer is defined by four properties. They work one layer below the teams' application code. They build and operate the foundation those teams ship through. They fan out across many teams, so their work is leverage that multiplies across everything shipping on it. And they own the path to production along with its guardrails.

My three roles are all cut on the same axis: which layer of the stack you compose into a shipping system. The AI Engineer builds primitives, the Manager of Agents composes a product with them, the AI-assisted engineer types alongside one. Every one of them is pointed at a shipping system. The horizontal role, the one that builds what other builders run on, is missing from all three. I left it off the list, and it turns out to be the one this whole bet leans on.
## The fourth role: Agent Platform Engineer
Map the four properties forward and the analog is hard to miss.

| DevOps-for-many-teams | Agentic-age analog |
| --- | --- |
| Works one layer below the app code | Works one layer below the product fleet; builds what the fleet-directors run on |
| Builds and runs the pipeline (runners, gates, policies) | Builds and runs the harness: eval loops, MCP gateways, cost and credit controls, policy gates, run observability |
| Serves multiple teams (fan-out) | Serves multiple agent-operating teams: a shared platform |
| Owns flow-to-prod plus guardrails | Owns the capability to ship safely; the shipped product belongs to the fleet-directors |

The cleanest name in current vocabulary is **Agent Platform Engineer** or **AI Platform Engineer**, with the ops-flavored variants **AgentOps** and **Agent SRE**. As far as I can find, none of them shows up with real job-posting volume yet. The function is being hired. The title has not caught up. That gap holds for every orchestration-tier label, and it holds for "Manager of Agents" too, which I coined and which nobody else has picked up. The work is visible. The names are still up for grabs.
## Two roles that look alike
This is the distinction I got wrong by omission, and it is worth being precise about, because the two roles look similar enough to blur together.

The Manager of Agents owns the accountability for what ships. The product. The features. The thing the customer uses and the thing the contract points at. The Agent Platform Engineer owns delivery capability. The harness. The eval loops, the cost ceilings, the policy gates, the kill switch ([the control-plane gap I wrote about before](./post/agent-governance-is-the-new-devsecops/)). They own whether the fleet can ship safely. The Manager of Agents owns what it ships.

Enablement and delivery are different jobs. That distinction is the whole point, and conflating the two is the hole the DevOps analogy exposes. A DevOps engineer enabling five teams owns the road those teams drive on. The cargo, the features, belongs to the teams. I had drawn three roles for the cargo and none for the road.
## DevOps already ran this experiment
Here is why this matters beyond taxonomy hygiene. The strongest attack on the original bet aimed past the name, straight at the dissolution thesis, and I owe it the strongest version I can write.

The argument goes like this. The Manager of Agents is a transitional phase that fades as the substrate matures. Agentic engineering, on this reading, is a way-station on the road to full agent orchestration. The economic gravity agrees. Anthropic's [Economic Index](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report) finds that work moving to the API skews directive, with less of a human in the loop than consumer use. Stripe's Minions team ships [over a thousand pull requests a week](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) with no human-written code, all human-reviewed, which Armin Ronacher and Mario Zechner would call the polite fiction at the heart of it. [Zechner's rule from the first piece](https://tldrecap.tech/posts/2026/aie-europe/pi-agent-minimalism/) still holds: if you don't read it, you don't own it. If the human role compresses to a rubber stamp on output nobody can actually read, then the orchestrator dissolves as the tooling matures, and the platform tier underneath it goes the same way.

That is the real argument, and answering it is the reason the fourth role matters.

DevOps is the historical counterexample. When CI/CD got easy, managed runners, golden paths, hosted pipelines, the role climbed the stack. It became platform engineering and the internal developer platform. The work was abstracted upward. Every time the commodity layer got cheaper, the judgment layer moved up a floor and the people went with it. If the agent-platform role is DevOps-shaped, that is the empirical answer to "it's a way-station." The dissolution thesis predicts that a mature substrate makes the human work disappear. The DevOps record shows the human work relocating upward. We have run this experiment once already.

There is an honest catch, in two parts, and skipping it would make this the kind of vendor argument I am trying not to write.

First, against the analogy. CI/CD is deterministic. Green or red, repeatable, the same inputs give the same result. Agent supervision is stochastic. Evals are probabilistic and the guardrails are soft. The clean "pipeline status" abstraction that made DevOps tractable does not transfer cleanly to a fleet of non-deterministic agents. That cut actually runs in favor of durability. Judgment that cannot be fully codified is harder to automate away. [Ronacher's phrase](https://mitsuhiko.github.io/talks/ai-engineer-talk/) is the sharp version: the friction is your judgment. The part of the platform role that is "which guardrails, what cost ceiling, what counts as acceptable risk in a TISAX or air-gapped environment" is exactly the part you cannot reduce to a YAML template.

Second, against me. Platform-as-code is itself a prime automation target. The repeatable wiring, the config, the boilerplate infrastructure, that is what agents are best at. So the commodity layer of the platform role compresses too, just like the typing did one floor down. What survives is the judgment layer. The plumbing gets generated like everything else. It is the same story as the engineer-to-orchestrator story from the first piece, moved up one level. I find that consistent. You may find it convenient. Hold that thought, because I am about to disclose why it is convenient for me specifically.

One more honest note before I do. [HBR](https://hbr.org/2026/02/to-thrive-in-the-ai-era-companies-need-agent-managers) and the enterprise-AI vendors already reached for the DevOps-and-SRE comparison: a role born from a technology shift that became a permanent fixture. They pinned it to a business-embedded agent manager, a PM-for-AI role. I think they grabbed the right analogy and pinned it one tier too high. The DevOps comparison fits the platform engineer, who does DevOps-shaped work for a living, more naturally than it fits a business-unit outcome owner.
## Disclosure
Now the disclosure, because it changes how you should read everything after it.

I work for [GitLab](https://about.gitlab.com/). GitLab sells the [Duo Agent Platform](https://docs.gitlab.com/ee/user/gitlab_duo/), and GitLab fields the kind of forward-deployed engineers I am about to discuss. My day job is being the platform engineer I just described: I build the usage controls, the credit and cost dashboards, the MCP governance, the eval and guardrail tooling that customers run their agents on. I am the Agent Platform Engineer archetype, in the flesh, and I am analyzing a market I sell into. That is probably why the missing role occurred to me at all. It is also why you should treat the next section as an argument to pressure-test before you accept it.
## Build versus rent has a third option
The decision everyone frames as build versus rent has a hidden third option, and naming it is the first useful move.

Should you hire an Agent Platform Engineer, or rely on your vendor's forward-deployed engineers to stand up the harness? Put that way, it sounds like a choice between two end states. It is really one path with two stages. The forward-deployed engineer is how the harness first gets built, and owning it is where that path leads. FDEs from the frontier labs and the platform vendors are a last-mile delivery function. They land, integrate with your stack, stand up the harness, prove value. Then they grow consumption, because that is what they are measured on. Making you self-sufficient is nobody's quota.

So "leave it to the FDEs" still builds the platform. It rents the platform-building capability and never takes delivery of it. The honest question is whether you plan the handoff to an internal owner or sleepwalk into permanent dependency. The decision turns on the handoff.
## Four drivers that settle it
Own it internally to the degree you score high on four drivers.

1. **Regulatory exposure.** TISAX, data residency, SOC2 ownership, sovereignty.
  
2. **Strategic centrality.** Are agents core to your product, or a side capability.
  
3. **Scale and rate of change.** How fast agent usage is growing and shifting.
  
4. **Switching-cost sensitivity.** How exposed you are to a single vendor's mental model.
  

For the verticals I work in, automotive, financial services, and government and defense, the first driver alone settles it. The accountability terminus has to stay where an auditor can demand to see who controls it. The default posture for those contexts has three moves: bootstrap with the FDE, own in steady state, and design the handoff from day one.
## The failure modes are asymmetric
I default to ownership in high-stakes contexts for one reason: the two failure modes are asymmetric.

|     | Hire internally (own) | Rent via vendor FDE |
| --- | --- | --- |
| Speed to value | Slower; learning curve on domain plus tooling | Fast; the FDE brings proven patterns |
| Accountability terminus | In-house, auditable, yours | Sits outside your org |
| Knowledge retention | Stays; operational resilience | Walks out when the engagement ends |
| Vendor lock-in | Lower; you can swap primitives | Deepens; the harness is built on the vendor's model of the world |
| Cost shape | Fixed; scarce, expensive talent | Opex; no hiring risk |
| Fits when | Agents are core, regulated, at scale | Agents are peripheral, early, needs unclear |
| Primary failure mode | Premature org chart | The cliff |

Look at the bottom row. The build-side failure is a premature org chart: you hired a dedicated platform engineer before the work justified the headcount. That failure is recoverable and self-correcting. You reassign the person, you absorb the cost, you move on. It announces itself in a budget review.

The rent-side failure is the cliff. The FDE rolls off, the engagement ends, and nobody internal can operate the harness they left behind. That failure is a latent operational and compliance liability. It does not announce itself. It surfaces only under stress: when an agent misbehaves in production, or when an auditor shows up. By the time you feel it, the person who built your guardrails is on another account.

One side fails loud and cheap. The other fails quiet, expensive, and at the worst possible moment. That asymmetry is the whole argument for defaulting to ownership when the stakes are high, even when renting is faster.
## The market rents where it can least afford to
Here is the part that should bother you if you sell this, and I do.

The field data on forward-deployed engineers shows adoption concentrated in regulated verticals. Roughly a quarter financial services, a fifth government and defense, a sixth healthcare. Needs verification: that breakdown traces to a single analysis of FDE postings, and I would not stake much on the exact splits. The concentration in regulated industries holds up across sources. The precise percentages rest on that single analysis.

Those are exactly the sectors where the accountability terminus is non-delegable. So the market is renting the agent platform in precisely the place where renting it carries a hidden compliance liability. The detonation is easy to picture. An auditor asks who controls the guardrails on the agents touching regulated data. The honest answer is "our vendor's engineer." The follow-up answer is "who is no longer on the account." That single exchange is the whole risk in one sentence.

There is a GitLab-native angle here, and I will state it as plainly as the disclosure demands. A single integrated platform shrinks the surface area of the harness an internal owner has to operate, compared to stitching point solutions into a bespoke orchestration layer. Less surface area lowers the bar to bringing the role in-house. That is a real argument for consolidation. It is also an argument I am paid to find persuasive, so weigh it accordingly. The structural point underneath it does not need my employer to be true: the smaller the harness an internal owner has to hold, the more likely the handoff actually happens.
## Three pushbacks I take seriously
A follow-up that does not name where it breaks is just a victory lap. Three pushbacks I take seriously.

The boundary might be a gradient. Maybe the Agent Platform Engineer collapses back into the Applied AI Engineer the moment that engineer composes primitives into a platform for many teams. If the only thing separating them is what you happen to be building this quarter, then I have dressed up a task as a job title. My defense is the fan-out: serving many teams is a structural difference that holds regardless of this quarter's work. I am still not certain the wall is as solid as I am drawing it.

The durability might be local. Maybe the dissolution thesis wins outright in non-regulated software, and the platform role stays durable only where compliance forbids unattended automation. That would make the role real but narrower than DevOps ever was: a regulated-industry specialty. I can live with that version. It is still a role my original taxonomy did not have.

The handoff might be a story enterprises tell themselves and never execute. "Bootstrap with the FDE, own in steady state" assumes the steady-state owning happens. If it usually does not, if permanent dependency is the realistic default, then the compliance liability I described is the base case, and it is larger than I am claiming.
## The close
The accountability terminus from the first piece turned out to have a physical address. It lives in the harness: the guardrails, the policy gates, the eval loops, the kill switch. That is the platform tier I left out, and naming it changes the build-versus-rent question into something sharper.

The build is rentable. Ownership of the accountability terminus stays in-house.

A vendor's engineer can construct your harness, integrate it, and prove it works. The one an auditor points at, when the agents touching regulated data do something nobody authorized, has to be someone who stays. The market is conflating those two roles right now, and it conflates them hardest in exactly the places where the bill comes due.

If you are running agents in a regulated enterprise: who controls your guardrails today, and is that a name you would be comfortable giving an auditor? If the answer is a vendor's engineer, do you have a handoff plan in writing? I want to hear from the people who have actually run this handoff, in either direction.
