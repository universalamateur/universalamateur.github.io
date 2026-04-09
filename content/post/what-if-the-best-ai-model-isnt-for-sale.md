---
title: "What If the Best AI Model Isn't for Sale?"
date: 2026-04-09
draft: false
tags: ["AI", "enterprise", "business model", "thought experiment"]
summary: "I ran a thought experiment on a hike. A company builds the most powerful AI model ever, then refuses to sell it. Two days later, I checked the news."
showtoc: false
---

Hiking above [Glyfada](https://en.wikipedia.org/wiki/Glyfada) last week, watching the Saronic Gulf from a ridge trail, I ran a thought experiment. What if an AI company builds the most powerful model ever created, then refuses to sell it? No public [API](https://en.wikipedia.org/wiki/API). No enterprise license. Instead, they deploy it themselves, through elite engineering teams embedded directly in your company, partnered with the consulting firms already sitting in your boardroom. You don't get the model. You get the results.

I thought this was wild speculation. Then I got home and checked the news.

## The model that isn't for sale

On April 7, 2026, [Anthropic](https://www.anthropic.com/) announced [Claude Mythos Preview](https://red.anthropic.com/2026/mythos-preview/). It is, by their own account, a step change in capabilities, a general-purpose frontier model that found thousands of previously unknown [zero-day vulnerabilities](https://en.wikipedia.org/wiki/Zero-day_(computing)) across every major operating system and web browser. [Anthropic will not make it generally available](https://www.nbcnews.com/tech/security/anthropic-project-glasswing-mythos-preview-claude-gets-limited-release-rcna267234). This is the first time in nearly seven years that a leading AI lab has publicly withheld a frontier model.

Instead of releasing it, Anthropic launched [Project Glasswing](https://www.anthropic.com/glasswing), a controlled deployment through partnerships including [Nvidia](https://www.nvidia.com/), [AWS](https://aws.amazon.com/), [Apple](https://www.apple.com/), [Google](https://cloud.google.com/), [Microsoft](https://www.microsoft.com/), [CrowdStrike](https://www.crowdstrike.com/), [Palo Alto Networks](https://www.paloaltonetworks.com/), and the [Linux Foundation](https://www.linuxfoundation.org/). Access is gated. You do not buy the model. You get invited into the program.

To be fair, a model that autonomously discovers zero-days in every major browser and operating system *cannot* be safely released on a public API. The gating is a legitimate security decision. But it is also, conveniently, a business model. Safety requires restricted access, and restricted access creates a monopoly on the most powerful capabilities in the market. Both things can be true at the same time.

## The consulting army

In December 2025, Anthropic signed a [multi-year partnership with Accenture](https://techcrunch.com/2025/12/09/anthropic-and-accenture-sign-multi-year-ai-strategic-partnership/), creating the Accenture Anthropic Business Group and training 30,000 Accenture employees on Claude. Two months earlier, they struck a deal with [Deloitte](https://www.deloitte.com/) to certify 15,000 staffers on the model for clients in regulated industries. In March 2026, Anthropic launched the [Claude Partner Network](https://thenextweb.com/news/anthropic-commits-100m-to-claude-partner-network) with $100 million in funding, bringing [Cognizant](https://www.cognizant.com/) and [Infosys](https://www.infosys.com/) into the fold.

That is 45,000+ consultants trained on one company's AI, deployed into client engagements worldwide. Not developers using an API. Trained practitioners embedding into your operations.

[OpenAI](https://openai.com/) is doing the same thing from the other side. In February 2026, they [partnered with](https://fortune.com/2026/02/23/openai-partners-with-mckinsey-bcg-accenture-and-capgemini-to-push-its-frontier-ai-agent-platform/) [McKinsey](https://www.mckinsey.com/), [Boston Consulting Group](https://www.bcg.com/) (BCG), [Accenture](https://www.accenture.com/), and [Capgemini](https://www.capgemini.com/) to push their Frontier AI agent platform into the enterprise. The two leading AI labs are not competing for API customers anymore. They are competing for consulting relationships.

## The private equity play

Here is where my hiking thought experiment gets uncomfortable, because reality has overtaken it.

[Anthropic is in talks](https://www.theinformation.com/articles/anthropic-talks-blackstone-pe-firms-form-ai-consulting-venture) with [Blackstone](https://www.blackstone.com/), [Hellman & Friedman](https://www.hfrp.com/), and [Permira](https://www.permira.com/) to create a joint venture, essentially a consulting and implementation arm that would embed engineers directly into portfolio companies. The venture could raise up to $1 billion, with Anthropic contributing roughly $200 million. Blackstone already holds approximately $1 billion in Anthropic equity from their February 2026 investment at a $350 billion valuation.

[OpenAI is in parallel talks](https://www.axios.com/2026/03/17/private-equity-openai-anthropic) with [Advent International](https://www.adventinternational.com/), [Bain Capital](https://www.baincapital.com/), [Brookfield](https://www.brookfield.com/), and [TPG](https://www.tpg.com/) for an even larger version of the same structure, reportedly valued at around $10 billion, a majority-owned subsidiary staffed with forward-deployed engineers, with the PE firms as minority investors and initial customers.

Read that again. The PE firms are not just funding these ventures. They are the distribution channel. Every portfolio company in their ecosystem becomes a potential deployment target for the most capable AI models on earth, models that are not available on the open market.

## The Palantir precedent

None of this is unprecedented. [Palantir](https://www.palantir.com/) built a $2.87 billion revenue business on exactly this model: deploy your own engineers, on your own stack, directly into production inside customer environments. They call them [Forward Deployed Engineers](https://fde.academy/blog/how-palantir-invented-the-forward-deployed-engineer-model), and the model works. Palantir's "try-before-you-buy" [AIP](https://www.palantir.com/platforms/aip/) (Artificial Intelligence Platform) Bootcamps collapsed sales cycles from six months to days, and their US commercial customer count surged 69% in a single quarter.

The logic is straightforward. A model that costs thousands of dollars per hour to run is not a [SaaS](https://en.wikipedia.org/wiki/Software_as_a_service) (Software as a Service) product. It is a service delivery mechanism. You do not hand someone a Ferrari and wish them luck on the Autobahn. You send a racing driver.

## The two-tier market

This is what a two-tier market looks like.

**Tier one:** You have a relationship with the AI lab. You get the gated models, the forward-deployed engineers, the consulting partners trained on the latest capabilities, the PE firm's capital to fund the transformation. You accelerate at a rate your competitors cannot match.

**Tier two:** You buy API access to last year's model. You hire your own engineers to figure it out. You self-host [Gemma 4](https://blog.google/technology/developers/gemma-4/) or [Qwen 3.5](https://qwenlm.github.io/blog/qwen3.5/) and try to close the gap with open-weight models and your own ingenuity. You compete against tier-one companies that are running Mythos-class capabilities with expert implementation, while you are prompt-engineering the best model you can get your hands on.

This is artificial scarcity as a business strategy, and it is not accidental. On April 4, three days before the Mythos announcement, Anthropic [cut off third-party agent tools](https://venturebeat.com/technology/anthropic-cuts-off-the-ability-to-use-claude-subscriptions-with-openclaw-and) from using Claude subscriptions. A $200-per-month Max subscription was powering $1,000 to $5,000 worth of agent compute through tools like [OpenClaw](https://openclaw.com/). The message was clear: if you want the full capabilities, you come through our channels.

## What I cannot figure out

The scenario I dreamed up on that ridge trail had one more element: the AI lab takes equity in the companies it transforms. Not just service fees, but ownership stakes. Profit from the growth you engineered.

That piece is not confirmed. The PE joint venture structure does not publicly include Anthropic taking equity in end clients. But the architecture supports it. When you have $200 million committed to a venture that embeds your engineers into companies and deploys your gated models to transform their operations, the distance between "consulting fee" and "equity stake" is one term sheet.

I do not know if Anthropic or OpenAI will cross that line. I do know that the incentive structure points directly at it. And if they do, we are looking at something the tech industry has never produced: a hybrid venture-consulting firm that uses proprietary AI as the engine for guaranteed returns on its own investments.

Is this the future of high-performance AI? A gated capability that you can only access through the right partnerships? Or is it a concentration of power that the market will eventually route around?

I genuinely do not know. But I am no longer speculating. The pieces are on the board.
