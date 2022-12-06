# My personal blog universalamateur.net powered byt Pelican on GitLab Pages

This is the README to my personal blog powered by the static site generator [HuGo](https://gohugo.io/hosting-and-deployment/hosting-on-gitlab/) using [GitLab Pages](https://gitlab.com/pages/hugo).
The result you can find on [universalamateur.net](https://universalamateur.net/) and [universalamateur.gitlab.io](https://universalamateur.gitlab.io/)

## Start with Hugo

```bash
hugo new site universalamateur.gitlab.io
cd universalamateur.gitlab.io
git init
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke themes/ananke
echo "theme = 'ananke'" >> config.toml
hugo server /D
```

## Implemented custom theme

## Local installation

### MacOS M1

```bash
brew install hugo
```

### Linux x86

```bash
sudo apt install hugo
```
