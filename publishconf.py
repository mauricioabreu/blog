#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import sys
sys.path.append(os.curdir)

from pelicanconf import *


SITEURL = 'https://blog.maugzoide.com'
RELATIVE_URLS = False
TIMEZONE = 'America/Sao_Paulo'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
