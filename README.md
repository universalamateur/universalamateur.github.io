# My personal blog Universalamateur.net powered by Hugo on GitLab Pages

This is the README to my personal blog powered by [Hugo](https://gohugo.io/hosting-and-deployment/hosting-on-gitlab/) Static Site Generator using [GitLab Pages](https://gitlab.com/pages/hugo).
The result you can find on [Universalamateur.net](https://Universalamateur.net/), [falko-sieverding.de](https://www.falko-sieverding.de/) and [Universalamateur.gitlab.io](https://Universalamateur.gitlab.io/)

## Settings in GitLab

- Naming the project username.gitlab.io, in my case `Universalamateur.gitlab.io` makes the page available under the domain [Universalamateur.gitlab.io](https://Universalamateur.gitlab.io/).
- Pages is activated in the project
- [Pages Access Control List](https://docs.gitlab.com/ee/user/project/pages/pages_access_control.html) is set with this public Project to everyone
- [Pages deployment for static site](https://docs.gitlab.com/ee/user/project/pages/getting_started/pages_ui.html) is set up and everything in the public folder is served to the visitor.

## Start with Hugo

### Requirements for local work

Install Git and Hugo, then pull the repo if it exists, otherwise clone it.
Then in the repo directory we update the git submodule for the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme.

#### MacOS

```bash
brew install hugo git
git -C Universalamateur.gitlab.io pull || git clone https://gitlab.com/Universalamateur/Universalamateur.gitlab.io.git
cd Universalamateur.gitlab.io
git submodule update --init --recursive
```

#### Linux x86

```bash
sudo apt install git hugo -y
git -C Universalamateur.gitlab.io pull || git clone https://gitlab.com/Universalamateur/Universalamateur.gitlab.io.git
cd Universalamateur.gitlab.io
git submodule update --init --recursive
```

### Starting a local Hugo Webserver

```bash
hugo server -D -F
```

- The `-D` argument tells Hugo to include draft posts
- The `-F` argument tells Hugo to include future dated posts

### Initial one-time setup

Setting up the site and adding the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme.

```bash
hugo new site Universalamateur.gitlab.io
cd Universalamateur.gitlab.io
git init
git submodule add https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
hugo server -D
```

## Posting with Hugo

### Front matter (from `archetypes/post.md`)

```markdown
---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: true
tags: []
summary: ""
showtoc: true
---
```

### Cover images

1. Add the image to the folder `/static/images/`
2. Include in the front matter:
   ```yaml
   cover:
     image: '/images/NAME_OF_PICTURE.jpg'
   ```

### Folder structure

```
.
├── hugo.toml
├── archetypes
│   ├── default.md
│   └── post.md
├── content
│   ├── _index.md
│   ├── archives.md
│   ├── search.md
│   ├── about
│   │   └── index.md
│   └── post
│       └── *.md
├── static
│   └── images
└── themes
    └── PaperMod          (git submodule)
```

### Blog post creation

```bash
hugo new post/NAME-OF-POST.md
```

## Ideas for the future

### Tags parser

Write a python parser for a scheduled pipeline, which commits back into a md file the used tags and page count using those tags plus links.
