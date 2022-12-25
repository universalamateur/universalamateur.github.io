# My personal blog universalamateur.net powered by Hugo on GitLab Pages

This is the README to my personal blog powered by the static site generator [HuGo](https://gohugo.io/hosting-and-deployment/hosting-on-gitlab/) Static Site Generator using [GitLab Pages](https://gitlab.com/pages/hugo).
The result you can find on [universalamateur.net](https://universalamateur.net/), [falko-sieverding.de](https://www.falko-sieverding.de/ ) and [universalamateur.gitlab.io](https://universalamateur.gitlab.io/)

## Settings in GitLab

- Naming the project username.gitlab.io, in my case `universalamateur.gitlab.io` makes the page available under the domain [universalamateur.gitlab.io](https://universalamateur.gitlab.io/).
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
git -C universalamateur.gitlab.io pull || git clone https://gitlab.com/UniversalAmateur/universalamateur.gitlab.io.git
cd universalamateur.gitlab.io
git submodule update --init --recursive
```

#### Linux x86

```bash
sudo apt install git hugo -y
git -C universalamateur.gitlab.io pull || git clone https://gitlab.com/UniversalAmateur/universalamateur.gitlab.io.git
cd universalamateur.gitlab.io
git submodule update --init --recursive
```

### Initital One time Setup localy was

Setting up the Site and adding the [Theme Anake](https://github.com/theNewDynamic/gohugo-theme-ananke).

```bash
hugo new site universalamateur.gitlab.io
cd universalamateur.gitlab.io
git init
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke themes/ananke
echo "theme = 'ananke'" >> config.toml
hugo server /D
```

## Implemented custom theme
