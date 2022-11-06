# My personal blog universalamateur.net powered byt Pelican on GitLab Pages

This is the README to my personal blog powered by the static site generator [Pelican] using GitLab Pages.
The result you can find on [universalamateur.net](https://universalamateur.net/) and [universalamateur.gitlab.io](https://universalamateur.gitlab.io/)

## Implemented custom theme

To use a custom theme:

1. I picked the theme [bootlex](https://github.com/getpelican/pelican-themes/tree/master/bootlex).
2. For this to work I uncommented the following lines from my [`.gitlab-ci.yml`](https://gitlab.com/UniversalAmateur/universalamateur.gitlab.io/-/blob/main/.gitlab-ci.yml), replacing `<theme_name>` with the `bootlex`:

   ```yaml
   - svn export https://github.com/getpelican/pelican-themes/trunk/bootlex /tmp/bootlex
   - pelican-themes --install /tmp/bootlex
   ```

3. Edit [`pelicanconf.py`](https://gitlab.com/UniversalAmateur/universalamateur.gitlab.io/-/blob/main/pelicanconf.py) and add the theme:

   ```plaintext
   THEME = '/tmp/bootlex'
   ```

## Local installation

```bash
python3 -m venv .venv
./.venv/bin/pip install --upgrade pip
./.venv/bin/pip install pelican
svn export https://github.com/getpelican/pelican-themes/trunk/pelican-bootstrap3 /tmp/pelican-bootstrap3
pelican-themes --install /tmp/pelican-bootstrap3
source ./.venv/bin/activate
pelican -r -l
```

### MacOS M1

Special Instructions for MacOs

### Linux x86

Special Instructions for Linux

[pelican]: http://blog.getpelican.com/
