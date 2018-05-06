#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Site metadata
AUTHOR = u'Mauricio Antunes'
SITENAME = u'maugzoide'
SITETITLE = "Mauricio Antune's blog"
SITESUBTITLE = u'people, technology, culture'
SITELOGO = u'https://www.maugzoide.com/static/profile.png'
SITEURL = 'https://www.maugzoide.com'
MAIN_MENU = True
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'))
FAVICON = SITEURL + '/static/favicon.ico'
DEFAULT_PAGINATION = 10

# Content management
PATH = 'content'
THEME = 'pelican-themes/Flex'
STATIC_PATHS = ['static']

# Region settings
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets', 'gzip_cache']

# Social widget
SOCIAL = (('github', 'https://github.com/mauricioabreu'),
          ('twitter', 'https://twitter.com/maugzoide'),
          ('rss', '//blog.maugzoide.com/feeds/all.atom.xml'))
GOOGLE_ANALYTICS = 'UA-70804647-1'
DISQUS_SITENAME = 'maugzoide'
ADD_THIS_ID = 'ra-5695b2206aa8b571'
