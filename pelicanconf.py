#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'maugzoide'
SITENAME = u'maugzoide'
SITETITLE = 'maugzoide'
SITESUBTITLE = u'people, technology, culture'
SITELOGO = u'http://blog.maugzoide.com/static/profile.png'
SITEURL = ''

PATH = 'content'

THEME = 'theme'

MAIN_MENU = True

STATIC_PATHS = ['static']

FAVICON = SITEURL + '/static/favicon.ico'

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'))

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
PLUGINS = ['gzip_cache']

# Social widget
SOCIAL = (('github', 'https://github.com/mauricioabreu'),
          ('twitter', 'https://twitter.com/maugzoide'),
          ('rss', '//blog.maugzoide.com/feeds/all.atom.xml'))

DEFAULT_PAGINATION = 10
