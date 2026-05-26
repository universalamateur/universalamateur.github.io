---
title: "The Manager of Agents"
date: 2026-05-26
draft: false
tags: ["AI", "agents", "engineering", "DevTools", "Applied AI Engineering"]
summary: "A bet I am making with my career, written down so you can disagree with it. The unit of work in software engineering is moving from a human writing code to a fleet of agents writing it, and the human is becoming the manager of that fleet."
showtoc: true
---

This is a bet I am making with my career, written down so you can disagree with it.

The bet has three parts.

1. **The shift.** The unit of work in software engineering is moving from a human writing code to a fleet of agents writing it. The human is becoming the manager of that fleet: the decider on the hard problems, the reviewer of the critical code, and the master of the harness the fleet runs in.
2. **The role.** The work at that boundary is composition, not research or substrate-building, and that distinction is durable for at least five years. I am calling the role the *Applied AI Engineer*; from the platform side it has another name, the *Manager of Agents*. Same role, two names depending on where you stand.
3. **The platform.** The substrate underneath that role does not yet exist as a coherent product, and whoever ships it owns the next decade of devtools.

The piece below makes the case for each part, lists what the role needs, names three working engineers whose recent statements either back the bet or expose its weak spots, and ends with the part I am genuinely unsure about plus two predictions you can hold me to.

**Three terms used below.** A *harness* is the runtime shell around an agent: the sandbox, the tool access, the lifecycle hooks. A *1-way door* ([Bezos's term](https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders)) is an action you cannot undo: a production migration, a sent customer email, a rotated secret. A *2-way door* is reversible: a config change, a branch creation, a draft commit.

## Three vendors, same role

The platforms underneath the role are starting to admit it exists.

[Anthropic](https://www.anthropic.com/) ships a feature called [Auto Mode](https://www.anthropic.com/engineering/claude-code-auto-mode) that ranks an agent's proposed actions by blast radius, blocks the ones it judges *"irreversible and destructive,"* and terminates a whole session after three consecutive denials or twenty total blocks. [OpenAI Codex](https://developers.openai.com/codex/) names its agent-lifecycle interception points [`PreToolUse`, `PermissionRequest`, and `PostToolUse`](https://developers.openai.com/codex/hooks), and the docs are explicit that `PostToolUse` *"can't undo side effects from the tool that already ran."*

These are not two separate trends. They are two vendors converging on the same role. The role is the person whose job is no longer to write the code, but to direct the agents that write the code, and to own what those agents ship.

It is the person who opens a dashboard in the morning instead of an IDE. Some agents finished overnight work. Some hit a decision they want a human to make. Some ran past a budget and stopped. One pair of agents disagreed about an approach and needs a referee.

For the Staff engineer inside a company, this looks like a fleet of five to fifteen agents working through the team's backlog. The merge-request author is increasingly a process, not a person.

For the solo founder, it looks different. The fleet is the eight agents in their config that ship most of the code while the founder works on product positioning, customer calls, and the `AGENTS.md` files that encode the company's taste. There is no team to coordinate with. The agent fleet is the team.

## What I mean by Applied AI Engineer

I am not a researcher. I am not a foundational platform builder. I am a solution and harness builder. I sit in the layer above the LLM substrate that Anthropic, OpenAI, and [AWS](https://aws.amazon.com/bedrock/) ship, and below the customer problem the substrate has to serve.

I am the person whose work is composing existing AI primitives, LLMs, agents, [MCP servers](https://modelcontextprotocol.io/), vector stores, eval loops, into systems that solve real business problems and ship to real users. The substrate is what someone else built. The opportunity is what I can do with it now.

None of the existing labels carry the qualifier I need. Anthropic calls it agentic engineering. [Daniel Miessler](https://danielmiessler.com/) frames the principal layer above the fleet as [*"strategy, judgment, relationships, creative direction"*](https://danielmiessler.com/blog/personal-ai-infrastructure). [Peter Steinberger](https://steipete.me/) calls his daily-driver agent [*"the introverted engineer that chugs along and gets stuff done"*](https://steipete.me/posts/just-talk-to-it), but applied to a fleet. The vocabulary is open. I am picking *Applied AI Engineer* because the qualifier matters: this is engineering done in service of a real outcome, with the model and the agents as the means, not the end.

If others adopt the term, the bet on the vocabulary is right. If they pick a different name for the same role, I lose the vocabulary fight but win the role. If the bet is wrong, I will need a different name in a year. If the bet is right, this is the job.

## Seven things the role needs

Forget the marketing slides. Seven things break when your unit of work is a fleet, not a person.

**1. A safe place for their agents to run.** Anthropic frames it: [*"the harness also became cattle. Because the session log sits outside the harness, nothing in the harness needs to survive a crash."*](https://www.anthropic.com/engineering/managed-agents) The [same post on tokens](https://www.anthropic.com/engineering/managed-agents): *"make sure the tokens are never reachable from the sandbox where Claude's generated code runs."* Codex implements the same pattern with OS-native primitives: [Seatbelt on macOS, Bubblewrap on Linux, Windows Sandbox on Windows](https://developers.openai.com/codex/concepts/sandboxing).

Each agent gets its own ephemeral compute, the sandbox cannot reach a system the manager did not authorize, network egress is blocked by default, and a finished session disappears. The point is not that sandboxes constrain agents. The point is that good sandboxes *enable* delegation that would otherwise be irresponsible.

**2. The ability to see what their agents are doing.** Not after the fact in a postmortem. In real time, the way an SRE sees production traffic. Anthropic's [multi-agent research-system team is explicit](https://www.anthropic.com/engineering/multi-agent-research-system): *"adding full production tracing let us diagnose why agents failed and fix issues systematically,"* and the tracing watches *"decision patterns and interaction structures, all without monitoring the contents."*

The questions matter more than the metrics. Is the agent making progress toward the goal, or stuck? Show me the variants the agent considered, side by side. Is the agent staying in the clever zone, or [over-engineering its way out of it](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md)? The right heuristic for the over-engineering question lives in [the same multica-ai repo, as a community summary of Karpathy's principles](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/README.md): *"would a senior engineer say this is overcomplicated? If yes, simplify."* And: yesterday the agent knew your migration constraint; today the platform [compacted it out](https://developers.openai.com/codex/learn/best-practices). The dashboard has to surface that.

**3. A decision dashboard that respects their time.** Most of what agents do should not need a human. Codex [names the lifecycle hooks](https://developers.openai.com/codex/hooks) for blocking decisions before they execute (`PreToolUse`) versus reviewing them after (`PostToolUse`), and is honest about the asymmetry: post-tool review *"can't undo side effects from the tool that already ran."* That is what a 1-way door looks like in production today.

Anthropic Auto Mode classifies which actions are 1-way doors and gates the irreversible ones with explicit approval; it also admits a [17% false-negative rate](https://www.anthropic.com/engineering/claude-code-auto-mode) versus unguarded execution. Daniel Miessler describes the same shape from the principal side in [SPQA (State, Policy, Questions, Action)](https://danielmiessler.com/blog/spqa-ai-architecture-replace-existing-software): *"this is the guidance that comes from humans that we're using to steer the ACTION part. Even more than your STATE, the content of your POLICY will become the most unique and identifying part of your business."*

Comments are about the *output*, not the agent. Talking about the fleet as if it had moods (*"the agent was lazy today"*) corrupts the feedback signal the platform needs to improve.

**4. An experiment space.** A place to try a new prompt variant, a new skill, a new model choice against the team's last fifty Merge Requests and Issues, without affecting today's production work. Anthropic's [recommended quality loop is Writer / Reviewer subagents](https://code.claude.com/docs/en/best-practices) with separate context windows that *"report back summaries"* so the orchestrator never sees the noise. Codex's parallel-work failure mode is named explicitly: [*"running live threads on the same files without using git worktrees."*](https://developers.openai.com/codex/learn/best-practices) The manager-of-agents needs cheap branches, not bravery.

**5. A place to keep what their agents learned.** The fleet accumulates context. Which approaches worked. Which patterns failed. Which customer asks recur. If this knowledge lives only in scrollback, it is gone the moment a session compacts. Codex names the persistence layer: [`AGENTS.md` for project-local rules](https://developers.openai.com/codex/memories), plus a `Chronicle` memory layer and a `PreCompact` hook that intercepts what the platform is about to drop. The manager-of-agents writes the substrate that the agents read on every run.

**6. Authorization with the least possible risk.** Codex's guidance leads with the principle: [*"choose the narrowest profile that still lets the task complete,"*](https://developers.openai.com/codex/permissions) across three named profiles (`:read-only`, `:workspace`, `:danger-full-access`). Anthropic's Auto Mode uses the same shape: Tier 1 read-only, Tier 2 in-project edits reversible via git, Tier 3 classifier for high-risk acts. Each agent has its own identity, secrets the agent can reach live only for the session, when the agent needs elevated access it asks, the manager grants for that session, and the elevation is logged. The agent acts on the manager's behalf through a delegate identity, not by borrowing the manager's password.

**7. A kill switch.** Anthropic [ships four levels](https://code.claude.com/docs/en/best-practices) of stop-and-recover: `Esc` interrupts mid-action, `Esc+Esc` or `/rewind` restores both the prior conversation and the prior code state, checkpoints persist across sessions, and Auto Mode auto-aborts in non-interactive mode after repeated classifier blocks. *"Conversations are persistent and reversible. Use this to your advantage."* Codex ships the [remote kill-switch from the ChatGPT mobile app](https://developers.openai.com/codex/remote-connections) to a connected Mac.

## People doing the work are saying the same thing

If this were just my bet, you should be skeptical. It is not. Three engineers I respect are running fleets right now and saying parts of the same observation in their own vocabularies.

**Peter Steinberger** (ex-founder of [PSPDFKit](https://pspdfkit.com/), creator of [OpenClaw](https://github.com/openclaw/openclaw), now at OpenAI) wrote in October 2025: [*"agentic engineering has become so good that it now writes pretty much 100% of my code... I've completely moved to codex cli as daily driver. I run between 3-8 in parallel."*](https://steipete.me/posts/just-talk-to-it) He goes further: *"the more you work with agents, the better your results will be. Almost all of these are characteristics of senior software engineers."* In February 2026 he joined OpenAI [*"to work on bringing agents to everyone... my next mission is to build an agent that even my mum can use."*](https://steipete.me/posts/2026/openclaw)

**Mario Zechner** (creator of [libGDX](https://libgdx.com/), builder of [Pi](https://mariozechner.at/), the minimalist coding agent that became the substrate for Steinberger's OpenClaw) opened his [AI Engineer Europe 2026](https://www.ai.engineer/) talk in April with [*"slow the fuck down."*](https://tldrecap.tech/posts/2026/aie-europe/pi-agent-minimalism/) His Golden Rule: *"if it's critical, read every line. If it's important, write it by hand. Don't let the agent make the big decisions. Use them for tasks that are scoped, verifiable, and boring/non-critical."* And the punchline: *"if you don't read it, you don't own it."* Zechner built Pi specifically because [Claude Code](https://www.anthropic.com/claude-code) had piled on features until it was unpredictable; his bet is on harness minimalism so the human can stay accountable.

**Daniel Miessler** ([Unsupervised Learning](https://danielmiessler.com/)) frames the role from the principal side. His three-tier model: [*"humans... strategy, judgment, relationships, creative direction. Digital Assistants... personal AI systems. Digital Employees... work independently on assigned tasks."*](https://danielmiessler.com/blog/personal-ai-infrastructure) The escalation pattern, in his words: *"most stays at the bottom layer, humans only see what requires judgment."* And the warning shot in [Unsupervised Learning #529](https://newsletter.danielmiessler.com/p/unsupervised-learning-no-529) from May 12, 2026: *"autonomous AI agents can quietly create 'shadow admin' backdoors. Security teams miss it because the changes come from legit actions, so logs lack the context to connect the chain."* The role exists. The platform underneath it does not yet exist correctly. That is why the manager is needed.

## The recursion question

There is an obvious counter-argument to all of this, and [ThePrimeagen](https://youtu.be/u09QevnY2b4) put it on stream around the 8-minute mark, reacting to a tech executive's prediction that AI replaces all white-collar work in 12 to 18 months. His move was to draw the org chart and walk the recursion:

> *"There's a manager and there's ICs... The ICs go off and they do work... So what he's saying is that all of these within 12 to 18 months, AI is going to be capable to do all these positions... So then that means your manager would have to go from manager to some sort of agent master. Drives all the agents. Okay, let's just take this exact same picture and couldn't we just do that again? Meaning that instead of ICs right here, we have agent masters. The agent masters can just be automated because we can just simply have an agent master agent... If you can automate the bottom layer, you should be able to keep on automating all the way up. And so then my only question, isn't this guy's job? Didn't he just say within 12 to 18 months his job's gone?"*

The recursion is real, and ducking it weakens the case for the role. An agent that supervises an agent that supervises an agent is technically possible to build. Anthropic's orchestrator-worker pattern already does the first step.

The recursion *should* stop at accountability, not at capability. None of the substrate I have described (Auto Mode tiers, Codex permission profiles, audit logs, kill-switch ladders) *enforces* accountability terminus on its own; these are technical gates. The reason the line holds is that the agents inherit their goals, their risk tolerance, and their consequences from contracts they did not sign. Success criteria, acceptable risk, and 1-way-door consent originate outside the agents because the contracts and the legal exposure live outside the system. The substrate I named is what makes that normative line *defensible in practice*: an agent fleet running on tiered permissions, with audited 1-way-door gates and a working kill switch, can be honestly accountable to a human in a way that an ungoverned fleet cannot.

You can automate the rolls-down-the-hill management. You cannot automate the accountability terminus, because the human is the part the contracts point at. The Manager of Agents is the role at the boundary between what can recurse and what cannot. Primeagen's punchline lands precisely there: the chief scientist is *also* going to find out that what survives at the top of his recursive stack is not "white-collar work" but *the human who bears the consequence when the agents are wrong*.

The deeper version of the recursion challenge is the right one: most of "management" was already mostly translation work, and translation work is what agents are good at. The role this piece describes is what is left after the translation work is removed. Miessler's SPQA framework names the residue: POLICY is what the human keeps when ACTION goes to the fleet.

## Where I might be wrong

A bet that does not name where it could fail is not a bet, it is a sales pitch. Three pushbacks from working engineers are worth taking seriously.

**Zechner's pushback: fleet scale is not honest.** His position is that one human cannot truthfully supervise N agents producing 10x human throughput, because [*"if you don't read it, you don't own it"*](https://tldrecap.tech/posts/2026/aie-europe/pi-agent-minimalism/) and reading every line at fleet speed is a lie people tell themselves. The implication is that the role I am describing exists at scale 1-2, not at scale 5-15, and certainly not at the [Stripe-Minions 1300-PRs-a-week scale](https://blog.bytebytego.com/p/how-stripes-minions-ship-1300-prs). Bubble check: am I assuming throughput numbers that only work because nobody is reading the output?

**Stripe's pushback: fleet-scale already works without my role description.** Stripe's Minions team [ships 1,300 PRs/week from agents inside a single company](https://blog.bytebytego.com/p/how-stripes-minions-ship-1300-prs) ([architecture writeup on stripe.dev](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents)). If that works at production scale, then the bottleneck I describe (manager judgment, accountability terminus, 1-way-door gating) is either invisible to Stripe (which means they have solved it some way I have not seen) or absent (which means a sufficiently mature substrate dissolves the role). Bubble check: am I describing a transitional role that exists at the awkward middle of the adoption curve and disappears once the substrate matures?

**Miessler's pushback: I am extending an individual-layer pattern to enterprise without the data.** Miessler's [three-tier workforce](https://danielmiessler.com/blog/personal-ai-infrastructure) and [SPQA framework](https://danielmiessler.com/blog/spqa-ai-architecture-replace-existing-software) are about a single principal with an army of agents. The case for a single human managing a single fleet under a single set of policies is well-articulated. The case I am making is harder: in the enterprise version, the policy author, the agent operator, the auditor, and the accountable party are *different humans*, with different incentives and different exposure. That is a meaningfully different problem from the one Miessler is solving. Bubble check: am I claiming Miessler's validation when his framework actually does not cover the case I am betting on?

If any of these three pushbacks turn out to be load-bearing, the bet changes shape. Possibly the role is narrower than I am claiming, or the title Applied AI Engineer is right at the individual layer and wrong at the enterprise layer.

## What the bet is not

The bet is not that agents replace engineers; they replace the typing, not the engineering. The role I am describing is an IC role that emerges alongside Staff and Principal management, not instead of it.

The bet is not that the role pays Principal salary today; the salary lags the work, often by years. And no specific vendor wins by name; whoever ships the substrate first owns the lane.

## Two predictions you can hold me to

By **end of 2026** (about seven months from now), at least one major DevTools vendor will ship a product whose UX explicitly names the role I am describing. Not "AI coding assistant." Not "agent platform." Something closer to *Manager of Agents* or *agent operator*, or the term that emerges from the vocabulary fight Karpathy started.

By **end of FY27**, the role will appear on at least one public job posting at a regulated-enterprise scale: financial services, healthcare, or government.

My next deliverable in this thesis is the substrate side: a write-up of what the platform underneath the role has to provide, evaluated against the seven needs above. If the bet is right, that piece reads as a buyer's guide. If the bet is wrong, it reads as a postmortem.

The platform underneath this role is what the next decade of devtools builds. The role is real now. The platform that makes it tractable is what we ship next.

If you are running a fleet of agents, as an IC, as a founder, or as something we have not named yet, where is the platform failing you, and where do you think the bet above is wrong?

---

## Sidebar: what a `SKILL.md` (or `AGENTS.md`-style skill file) looks like

Five lines of YAML frontmatter from the [multica-ai/andrej-karpathy-skills repo](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/skills/karpathy-guidelines/SKILL.md) showing the artifact-shape:

```yaml
---
name: karpathy-guidelines
description: Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code.
license: MIT
---
```

Kebab-case name. One-sentence description that doubles as the trigger heuristic for the agent. Licensable, shippable, versionable. The body underneath is the four-principle Karpathy discipline: Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution.

**Practical note.** Harnesses (Claude Code Skills, Codex skill discovery) read the `description` field at trigger-evaluation time. That makes a skill file *executable config in disguise*. Review the YAML of any third-party skill before installing it, the same discipline you would apply to a CI workflow file.

---

## Source map

| Source | What it grounds |
|---|---|
| [Anthropic Auto Mode](https://www.anthropic.com/engineering/claude-code-auto-mode) | Blast-radius classifier, 17% false-negative rate |
| [Anthropic Managed Agents](https://www.anthropic.com/engineering/managed-agents) | "Harness also became cattle"; "tokens never reachable from the sandbox where Claude's generated code runs" |
| [Anthropic Sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing) | Sandbox-as-force-multiplier |
| [Anthropic Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system) | Decision-patterns tracing without content monitoring |
| [Anthropic Best Practices](https://code.claude.com/docs/en/best-practices) | Esc / /rewind kill-switch ladder; Writer / Reviewer subagent |
| [OpenAI Codex Hooks](https://developers.openai.com/codex/hooks) | PreToolUse / PermissionRequest / PostToolUse / PreCompact lifecycle |
| [OpenAI Codex Best Practices](https://developers.openai.com/codex/learn/best-practices) | Worktrees failure mode; auto-compact context loss |
| [Codex Permissions](https://developers.openai.com/codex/permissions) | Three named profiles; narrowest-profile principle |
| [Codex Memories](https://developers.openai.com/codex/memories) | AGENTS.md + Chronicle + PreCompact |
| [Codex Remote Connections](https://developers.openai.com/codex/remote-connections) | Mobile-to-Mac remote connections |
| [Codex Sandboxing](https://developers.openai.com/codex/concepts/sandboxing) | Seatbelt / Bubblewrap / Windows Sandbox |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Community summary of Karpathy's success-criteria framing; "would a senior engineer say this is overcomplicated"; YAML frontmatter |
| [Peter Steinberger, Just Talk To It](https://steipete.me/posts/just-talk-to-it) | "100% of my code"; "3-8 in parallel"; "characteristics of senior software engineers" |
| [Peter Steinberger, OpenClaw / OpenAI move](https://steipete.me/posts/2026/openclaw) | OpenAI hire Feb 2026; "agent that even my mum can use" |
| [Mario Zechner, Pi at AI Engineer Europe](https://tldrecap.tech/posts/2026/aie-europe/pi-agent-minimalism/) | "Slow the fuck down"; Golden Rule; "if you don't read it, you don't own it" |
| [Daniel Miessler, Personal AI Infrastructure](https://danielmiessler.com/blog/personal-ai-infrastructure) | Three-tier workforce; "most stays at the bottom layer" |
| [Daniel Miessler, SPQA](https://danielmiessler.com/blog/spqa-ai-architecture-replace-existing-software) | POLICY as the human-encoded steering layer |
| [Daniel Miessler, UL #529](https://newsletter.danielmiessler.com/p/unsupervised-learning-no-529) | Shadow-admin quote |
| [ByteByteGo, How Stripe's Minions Ship 1300 PRs](https://blog.bytebytego.com/p/how-stripes-minions-ship-1300-prs) | 1,300 PRs/week field number |
| [Stripe Dev Blog, Minions architecture](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) | Architecture writeup |
| [ThePrimeagen clip](https://youtu.be/u09QevnY2b4) | Recursion riff 7:52-9:58 |
| [Jeff Bezos 1997 shareholder letter](https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders) | 1-way / 2-way door framing |
