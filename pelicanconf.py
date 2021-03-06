#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jamie Duncan'
SITENAME = u'Open Tech Podcast'
SITEURL = 'https://opentechpodcast.org'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'opetechpodcast.org'
CATEGORY_FEED_ATOM = 'feeds/all.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_RSS = 'feeds/rss.xml'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = "pelican-theme"
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['asciidoc_reader',
            'sitemap',
            'gravatar',
            'filetime_from_git',
            'gallery',
            'thumbnailer',
            'disqus_static',]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/CNAME'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'}
}


# nice-blog them settings
SIDEBAR_DISPLAY = ['about','links','categories','tags']
SIDEBAR_ABOUT = "Jamie Duncan and Dave Sirrine. A couple of career Open Source Geeks talking about technology with their friends, and an occassional beer."
THEME_COLOR = 'red'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

# thumbnailer settings
IMAGE_PATH = 'images'
THUMBNAIL_DIR = 'images'
THUMBNAIL_KEEP_NAME = True
THUMBNAIL_KEEP_TREE = True

# disqus_static settings
DISQUS_SITENAME = 'opentechpodcast'
DISQUS_PUBLIC_KEY = 'Zuy9Hu0Lj35N0FNLnke5ye9No0cJhsBvZKNGJ701eIJQf4adgeKYnGeROOHm1OgG'
DISQUS_SECRET_KEY = 's8BQwXKdKek2WAAHeIGAo9yzQrAMFDGjmBr3OmYq5IewowmeASmPllkUlkYRipVs'

ASCIIDOC_BACKEND = 'html5'

GALLERY_PATH = 'images/gallery'
RESIZE = [
        ('images/gallery', False, 200,200),
      ]

GOOGLE_ANALYTICS = 'UA-90496768-1'
