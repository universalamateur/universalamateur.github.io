# AGENTS.md

Hugo static site (PaperMod theme) deployed to GitLab Pages and GitHub Pages.

## Commands

```bash
# Dev server (drafts + future posts)
hugo server -D -F

# Build (matches CI)
hugo --minify

# New blog post
hugo new post/my-post-title.md
```

## Setup

Theme is a git submodule — must be initialized before building:

```bash
git submodule update --init --recursive
```

Hugo **0.160.0 extended** is required (pinned in both `.gitlab-ci.yml` and `.github/workflows/hugo.yml`).

## Content

- Posts go in `content/post/` (not `posts/`).
- Post archetype (`archetypes/post.md`) sets `draft: true`, `showtoc: true`, empty `tags[]` and `summary`.
- No custom layouts — all rendering comes from the PaperMod theme in `themes/PaperMod/`.
- Static images go in `static/` (referenced as `/images/foo.jpg` in content).

## Config

- Site config is `hugo.toml` (not `config.toml` — the README references `config.toml` but that is historical).
- `baseURL` is set to the GitLab Pages URL; GitHub Actions overrides it with `--baseURL` at build time.
- JSON output is enabled on the home page for PaperMod's Fuse.js search.

## CI/CD

- **GitLab CI** (`.gitlab-ci.yml`): `pages` job deploys on default branch; `test` job validates builds on all other branches.
- **GitHub Actions** (`.github/workflows/hugo.yml`): mirrors deployment to GitHub Pages on push to `main`.
- Both install Hugo from the same pinned version. Keep them in sync when upgrading.
