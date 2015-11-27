#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'maugzoide'
SITENAME = u'maugzoide'
SITEURL = ''

PATH = 'content'

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
SOCIAL = (('Github', 'https://github.com/mauricioabreu'),
          ('Twitter', 'https://twitter.com/maugzoide'),)

DEFAULT_PAGINATION = 10
