# My personal blog Universalamateur.net powered by Hugo on GitLab Pages

This is the README to my personal blog powered by [HuGo](https://gohugo.io/hosting-and-deployment/hosting-on-gitlab/) Static Site Generator using [GitLab Pages](https://gitlab.com/pages/hugo).
The result you can find on [Universalamateur.net](https://Universalamateur.net/), [falko-sieverding.de](https://www.falko-sieverding.de/ ) and [Universalamateur.gitlab.io](https://Universalamateur.gitlab.io/)

## Settings in GitLab

- Naming the project username.gitlab.io, in my case `Universalamateur.gitlab.io` makes the page available under the domain [Universalamateur.gitlab.io](https://Universalamateur.gitlab.io/).
- Pages is activated in the project
- [Pages Access Control List](https://docs.gitlab.com/ee/user/project/pages/pages_access_control.html) is set with this public Project to everyone
- [Pages deployment for static site](https://docs.gitlab.com/ee/user/project/pages/getting_started/pages_ui.html) is set up and everything in the public folder is served to the visitor.

## Start with Hugo

### Rquirements for local work

We isntall Git and Hugo, then pull the repo is it exists, otherwise clone it.
Then in the repo directory we update the git submodule there, the theme Anake for hugo.

#### MacOS M1

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

### Starting a local Hogu Webserver

```bash
hugo server -D -F
```

- The -D argument tells Hugo to include draft post
- The -F argument tells Hugo to include future dated post that are published

### Initital One time Setup localy was

Setting up the Site and adding the [Theme Anake](https://github.com/theNewDynamic/gohugo-theme-ananke).

```bash
hugo new site Universalamateur.gitlab.io
cd Universalamateur.gitlab.io
git init
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke themes/ananke
echo "theme = 'ananke'" >> config.toml
hugo server /D
```

### Implemented custom theme

At the moment using Anake, Future our own theme based on Anake

## Posting with Hugo

### Used Front Matter in Articles by default

```markdown
---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date | time.Format ":date_long" }}
draft: true
tags: []
featured_image: ""
description: ""
---
```

#### featured image

1. Add the image to the folder `/static/images/`
2. include in the Front Matter: `featured_image: '/images/NAME_OF_PICTURE.jpg'`
3. to hide the header text on the featured image on a page, set in Fornt Matter `omit_header_text: true`

### Folder Structure after setup

```markdown
.
├── config.toml
├── archetypes
│   ├── default.md      // default archetype for all articles
│   └── post.md         // Declared archetype for posts
├── content
│   ├── _index.md       // Overwriting the initial Landing page with pst listing
│   ├── about
│   │   └── index.md    // Bio and Portfolio Page
│   └── post
│       ├── Blog-Setup-with-Hugo-on-GitLab.md   // A Technical BLog Article
│       ├── My-Lasagna-recipe.md                // Post with recipes
│       └── The-Initial-Post.md                 // and other Articles
├── static
│   └── images          // Folder for prepared images
│       └── SunDown.jpg
```

### Archetypes

### Blog Post Creation Commands

- `hugo new post/NAME-OF-POST.md`

## Ideas for the future

### Used tags parser

Write a python parser for a sheculed pipeline, which commits back into a md file the used tags and pages number used those tags plus links on
