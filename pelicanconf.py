#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Universalamateur'
SITENAME = 'Blog Universalamateur'
SITEURL = 'https://universalamateur.gitlab.io'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Links to come in the future', '#'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/falko-sieverding-universalamateur/'),
          ('Twitter (@falkosieverding)', 'https://twitter.com/falkosieverding'),
          ('BoardGameGeek (@zwobot)', 'https://boardgamegeek.com/user/zwobot'),)

DEFAULT_PAGINATION = 10

# Adding a custom theme
THEME = '/tmp/blue-penguin'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
