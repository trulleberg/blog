#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hannes Bellmer'
SITENAME = u'nanu'
SITEURL = u'http://blog.bellmer.org'

PATH = 'content'

TIMEZONE = u'Europe/Berlin'

DEFAULT_LANG = u'de'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feed/atom.xml'
FEED_ALL_RSS = 'feed/rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ( ('Pelican', 'http://getpelican.com/')
        ,)

# Social widget
SOCIAL = ( ('twitter', 'https://twitter.com/hannes_eins'),
           ('github', 'https://github.com/trulleberg'),
           ('xing', 'https://www.xing.com/profile/Hannes_Bellmer')
          ,)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "/Users/hannes/blog/pelican-themes/foundation-default-colours"
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
FOUNDATION_FRONT_PAGE_FULL_ARTICLES = True
FOUNDATION_ALTERNATE_FONTS = False
FOUNDATION_TAGS_IN_MOBILE_SIDEBAR = True
FOUNDATION_FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican</a> and <a href="http://foundation.zurb.com/">Zurb Foundation</a>. <br> Theme by <a href="http://hamaluik.com">Kenton Hamaluik</a> with smaller modifications by <a href="https://github.com/trulleberg/pelican-themes/tree/master/foundation-default-colours"> Hannes.</a>'
FOUNDATION_PYGMENT_THEME = 'monokai'

PLUGIN_PATHS = ['/Users/hannes/blog/pelican-plugins']
PLUGINS = ['i18n_subsites', ]

I18N_SUBSITES = {
        'en': {
            'SITENAME': 'nanu_en',
            'LOCALE': 'en_US', #This is somewhat redundant with DATE_FORMATS, but IMHO more convenient
            }
        }
languages_lookup = {
             'en': 'English',
             'de': 'Deutsch',
             }

def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]

JINJA_FILTERS = {
             'lookup_lang_name': lookup_lang_name,
             }
