#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'The Atlas Project'
SITENAME = 'The Atlas Project'
SITEURL = 'https://theatlasproject.org'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Got Questions?', 'https://www.gotquestions.org/'),
         ('Desiring God', 'https://www.desiringgod.org/'),
         ('The Bible Project', 'https://thebibleproject.com/'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#FilePaths
THEME = 'theme'
PLUGIN_PATHS = ['plugins', ]
PLUGINS = ['i18n_subsites', ]
ARTICLES_PATHS = ['articles']
STATIC_PATHS = ['img', 'pdf']
PAGE_PATHS = ['pages']

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

#Bootstrop Theme

BOOTSTRAP_THEME  = 'readable'

#Date format
DEFAULT_DATE_FORMAT =''

#Content Lisenscing: CC-BY
CC_LICENSE = 'CC-BY'

SHOW_ARTICLE_AUTHOR = True


#Social media
SHARIFF = True
SHARIFF_LANG = 'en'
SHARIFF_ORIENTATION = 'vertical'
SHARIFF_SERVICES = "[&quot;facebook&quot;,&quot;twitter&quot;]"
SHARIFF_THEME = 'white'

SITELOGO = 'img/atlas_filler_logo.png'
SITELOGO_SIZE = '32'

FAVICON = 'img/favico.png'

#Cache Settings
#CACHE_CONTENT = False
#LOAD_CONTENT_CACHE = False
