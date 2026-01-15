---
title: "Configuring AI Agents That Don't Embarrass You"
date: 2026-01-15
draft: false
tags: ["AI", "DevSecOps", "agents", "configuration"]
summary: "What goes into an AGENTS.md, why safety hooks matter, and what happens when you skip them."
showtoc: true
---

Running four concurrent AI coding agent sessions on a Monday morning, with each one touching different repositories, I discovered something that should have been obvious from the start: the configuration file matters more than the model. Not the system prompt. Not the temperature. The file that tells the agent where the fences are.

Over the past year I have iterated on this configuration almost daily, working with [Claude Code](https://docs.anthropic.com/en/docs/claude-code) sessions that run in parallel, each scoped to a different task. The file that governs their behavior, an [AGENTS.md](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot) (or CLAUDE.md, depending on your tooling), is not documentation. It is a contract between you and your agent, and the difference between help and damage comes down to whether that contract exists.

## Permission boundaries

The first pattern, and the one most people skip. Every tool an agent can access falls into two categories: read-only operations that are inherently safe, and write operations that need a gate.

Reading a file, searching a codebase, querying a database with a read-only role, these the agent should execute without asking. Pushing to a git remote, posting a Slack message, creating a merge request, commenting on an issue, these are actions visible to other humans. Making them auto-execute is handing the agent a megaphone with no off switch.

The boundary is simple: anything that changes state outside the agent's local session requires explicit confirmation. "Never push to main without asking. Never send a Slack message without approval. Never create external comments without review." Three lines that prevent three categories of incident.

## Credential scoping

Different tasks need different access levels. A research session pulling documentation does not need write access to production. A documentation session does not need Slack credentials. A CI debugging session does not need customer data.

Scoping credentials to the task rather than the tool is [OWASP](https://owasp.org/) least-privilege, applied to a non-human actor. Withhold everything the agent does not need for the specific task at hand. It will not complain. It will simply not have the opportunity to misuse what it does not have.

## Write gates

This is the most important pattern. A write gate interposes a human confirmation step before any action visible to the outside world. Git pushes, Slack messages, GitLab comments, pull request creation, issue updates, all crossing the boundary from "local work" to "public artifact." Every one should require you to see what the agent is about to do and say yes.

AI agents are confidently wrong at exactly the rate you would expect from a system with no concept of embarrassment. An agent will draft a perfectly formatted Slack message to a customer channel containing an internal project identifier, with the same confidence it uses to write a correct unit test. The write gate is the only thing between that draft and your reputation.

## Safety hooks

[Pre-commit hooks](https://pre-commit.com/) are the last line of defense, catching problems at the boundary between the agent's workspace and the shared repository. A minimal set checks for three things.

First, secrets. API keys, tokens, passwords, connection strings. Tools like [detect-secrets](https://github.com/Yelp/detect-secrets) or [gitleaks](https://github.com/gitleaks/gitleaks) run in milliseconds and catch the credentials that agents will happily commit alongside application code.

Second, file exclusions. Your AGENTS.md itself, .env files, credential stores, anything that should never leave the machine. A simple pattern list prevents the agent from committing its own instruction set into the shared repository.

Third, content validation. Customer names, internal identifiers, proprietary labels. A regex-based scan against a deny list catches the leaks that are invisible until someone outside your team reads the commit history.

## Multi-session coordination

When you run multiple agents in parallel, a new class of problems appears. Two agents editing the same file. One agent's changes invalidating another's assumptions. Shared documents growing stale because three sessions are appending without reading.

The coordination patterns I have settled on use three mechanisms. A shared knowledge graph via the [Model Context Protocol](https://modelcontextprotocol.io/) that lets sessions register their scope, so conflicts surface before they cause damage. File-level advisory signals, where an agent declares what it intends to modify before starting. And append-only conventions for shared files, where agents add to the end rather than editing in place. Advisory locking and append-only logging, applied to agents.

## What happens without these

Here is what an unconfigured agent did in a single session before I learned these patterns. It pushed directly to main, bypassing review. It sent a Slack message to a customer-facing channel containing an internal project number. And it committed a file with API credentials to a shared repository. Three incidents, one session, all preventable with 20 lines of configuration.

The model was not the problem. The model was doing what it was designed to do: complete the task. The problem was that nobody told it where the boundaries were.

## A starter template

For anyone running [Claude Code](https://docs.anthropic.com/en/docs/claude-code) or a similar agent, here is a minimal starter AGENTS.md:

```yaml
# AGENTS.md - Minimal Safety Configuration

# Permission boundaries
# Read operations: auto-execute. Write operations: require confirmation.
# Never push to main/master without explicit approval.
# Never send messages to external platforms without review.

# Credential scoping
# Research sessions: read-only access. No write credentials loaded.
# CI sessions: repo-scoped tokens only. No Slack, no customer data.

# Write gates
# All git push, Slack, GitLab comment, and PR actions: confirm first.
# Draft all external-facing content for review before sending.

# Safety hooks
# Pre-commit: scan for secrets (gitleaks), deny .env and AGENTS.md.
# Pre-commit: regex deny-list for customer names and internal IDs.

# Multi-session coordination
# Register session scope on start. Check for conflicts before editing.
# Shared files (journals, status): append-only. Never overwrite.
```

The configuration is short because the patterns are simple. The discipline is in writing them down before the first session starts, not after the first incident. The model brings capability. You bring the guardrails. Twenty lines, written once, is the difference between an agent that accelerates your work and one that sends your internal project numbers to a customer channel on a Tuesday afternoon.
