---
title: "Blog Setup With Hugo on GitLab and GitHub Pages"
date: 2022-12-26
lastmod: 2026-04-09
draft: false
tags: ["GitLab", "GitHub", "Hugo", "tutorial"]
summary: "Running a personal blog on Hugo with PaperMod, deployed to both GitLab Pages and GitHub Pages via push mirror."
showtoc: true
---

> Originally written December 2022 using the [Ananke](https://github.com/theNewDynamic/gohugo-theme-ananke) theme and `config.toml`. Rewritten April 2026 after migrating to [PaperMod](https://github.com/adityatelange/hugo-PaperMod) with dual CI/CD and a push mirror.

## Why Hugo and GitLab Pages

[Hugo](https://gohugo.io/) is a static site generator written in [Go](https://go.dev/). It compiles markdown files into a complete website in milliseconds, requires no runtime, no database, and no server-side processing. The output is plain HTML, CSS, and JavaScript, served by [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/) (and now also [GitHub Pages](https://pages.github.com/)) at zero cost.

Naming the repository `username.gitlab.io` makes the site available at `https://username.gitlab.io/` automatically. Pages is enabled in the project settings, access control is set to "Everyone," and everything in the `public/` build directory is served to visitors.

## Theme: PaperMod

The site uses [PaperMod](https://github.com/adityatelange/hugo-PaperMod), a clean, fast, responsive Hugo theme with dark mode, search, reading time, table of contents, and code copy buttons out of the box. It replaced the original [Ananke](https://github.com/theNewDynamic/gohugo-theme-ananke) theme in April 2026.

PaperMod is added as a Git submodule:

```bash
git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
```

## Configuration

Hugo configuration lives in `hugo.toml` (Hugo dropped support for `config.toml` as the default name in newer versions). The key settings:

```toml
baseURL = "https://universalamateur.gitlab.io/"
title = "Universalamateur"
theme = "PaperMod"
paginate = 10

enableRobotsTXT = true
buildDrafts = false

[params]
  env = "production"
  author = "Falko Sieverding"
  defaultTheme = "auto"        # light/dark follows system preference
  ShowReadingTime = true
  ShowBreadCrumbs = true
  ShowCodeCopyButtons = true
  ShowPostNavLinks = true
  showtoc = true

[taxonomies]
  tag = "tags"

[outputs]
  home = ["HTML", "RSS", "JSON"]  # JSON enables PaperMod's search
```

The `[outputs]` section is important: PaperMod's built-in search requires a JSON index, which Hugo only generates if you explicitly request it.

## Directory Structure

```text
.
├── hugo.toml                      # Site configuration
├── .gitlab-ci.yml                 # GitLab Pages deployment
├── .github/workflows/hugo.yml     # GitHub Pages deployment
├── content/
│   ├── _index.md                  # Landing page
│   ├── about/index.md             # About page (leaf bundle)
│   ├── post/                      # Blog posts
│   │   ├── the-token-salary-tipping-point.md
│   │   └── ...
│   ├── archives.md                # Archive page (PaperMod layout)
│   └── search.md                  # Search page (PaperMod layout)
├── static/                        # Images and other assets
│   └── images/
└── themes/PaperMod/               # Theme (git submodule)
```

Posts go in `content/post/` with lowercase hyphenated filenames. Each post uses this frontmatter:

```yaml
---
title: "Post Title"
date: 2026-04-09
draft: false
tags: ["AI", "DevSecOps"]
summary: "One-line summary shown in post listings."
showtoc: true
---
```

## Dual CI/CD: GitLab and GitHub Pages

The site deploys to both [GitLab Pages](https://universalamateur.gitlab.io) and [GitHub Pages](https://universalamateur.github.io) from the same repository. GitLab is the primary, and a [push mirror](https://docs.gitlab.com/ee/user/project/repository/mirror/push.html) syncs every commit to GitHub automatically.

### GitLab CI

```yaml
image: debian:bookworm-slim

variables:
  HUGO_VERSION: "0.160.0"
  GIT_SUBMODULE_STRATEGY: recursive

pages:
  before_script:
    - apt-get update && apt-get install -y --no-install-recommends wget ca-certificates
    - wget -q -O hugo.deb "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb"
    - dpkg -i hugo.deb
  script:
    - hugo --minify
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
```

The `debian:bookworm-slim` image matters: Hugo Extended requires [glibc](https://en.wikipedia.org/wiki/Glibc), which Alpine does not provide. An earlier version used Alpine and failed with a cryptic binary compatibility error.

### GitHub Actions

The GitHub workflow (`.github/workflows/hugo.yml`) runs the same Hugo version, triggered by the push mirror:

```yaml
name: Deploy Hugo site to GitHub Pages
on:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    env:
      HUGO_VERSION: 0.160.0
    steps:
      - name: Install Hugo CLI
        run: |
          wget -O ${{ runner.temp }}/hugo.deb \
            https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb
          sudo dpkg -i ${{ runner.temp }}/hugo.deb
      - uses: actions/checkout@v4
        with:
          submodules: recursive
      - uses: actions/configure-pages@v5
      - run: hugo --minify --baseURL "${{ steps.pages.outputs.base_url }}/"
      - uses: actions/upload-pages-artifact@v3
        with:
          path: ./public
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
    steps:
      - uses: actions/deploy-pages@v5
```

### Push Mirror Setup

The push mirror is configured in the GitLab repository under Settings > Repository > Mirroring. The mirror URL uses a GitHub [fine-grained personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#fine-grained-personal-access-tokens) with `contents: write` scope on the target repository. Every push to GitLab automatically propagates to GitHub, which triggers the GitHub Actions workflow.

## Local Development

### Prerequisites

```bash
# macOS
brew install hugo git

# Linux (Debian/Ubuntu)
sudo apt install git
# Install Hugo Extended from GitHub releases (apt version is usually outdated)
wget -O hugo.deb "https://github.com/gohugoio/hugo/releases/download/v0.160.0/hugo_extended_0.160.0_linux-amd64.deb"
sudo dpkg -i hugo.deb
```

### Clone and Run

```bash
git clone https://gitlab.com/UniversalAmateur/universalamateur.gitlab.io.git
cd universalamateur.gitlab.io
git submodule update --init --recursive
hugo server -D
```

The `-D` flag includes draft posts. The local server runs at `http://localhost:1313/` with live reload.

### Creating a New Post

```bash
hugo new post/my-new-post.md
```

This creates a file in `content/post/` with the default frontmatter. Set `draft: false` when ready to publish, commit, and push. Both pipelines handle the rest.
