#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hendrik Schawe'
SITENAME = 'Hendrik Schawe'
# SITESUBTITLE = 'lorem ipsum dolor sit amet'
SITEURL = 'https://hendrik.schawe.me'

from events import EVENTS
from publications import PUBLICATIONS, PREPRINTS

TYPOGRIFY = True

DATE_FORMATS = {
    'de': '%d.%m.%Y',
    'en': '%m/%d/%Y',
}

DEFAULT_METADATA = {
    'status': 'draft',
}

THEME = 'themes/purepelican'
from themes.purepelican.settings import *

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    "assets",
    "i18n_subsites",
    "doi_details",
]

DEFAULT_LANG = "de"
I18N_SUBSITES = {
    # 'de': {
    #     'SITE_DESCRIPTION': 'Hendrik Schawe',
    # }
    'en': {
        'SITE_DESCRIPTION': 'Hendrik Schawe',
    }
}

JINJA_ENVIRONMENT = {"extensions": ['jinja2.ext.i18n']}

READERS = {"html": None}
STATIC_PATHS = [
    'extra/manifest.json',
    'extra/favicon.ico',
    'extra/icons',
    'extra/googlee1eadb2ddedaa639.html',
    'extra/BingSiteAuth.xml',
    'extra/cname',
    'extra/sitemap.xml',
    'extra/robots.txt',
    'extra/legacy_redirect.html',
    'img',
    'pdf',
]

EXTRA_PATH_METADATA = {
    'extra/manifest.json': {'path': 'manifest.json'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/googlee1eadb2ddedaa639.html': {'path': 'googlee1eadb2ddedaa639.html'},
    'extra/BingSiteAuth.xml': {'path': 'BingSiteAuth.xml'},
    'extra/cname': {'path': 'CNAME'},
    'extra/sitemap.xml': {'path': 'sitemap.xml'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/legacy_redirect.html': {'path': 'de/index.html'},
}

SITE_DESCRIPTION = 'Hendrik Schawe'
FEATURED_IMAGE = 'https://blog.schawe.me/img/logo.png'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
# (linktext, link, [font awesome symbol])
SOCIAL = (
    ('GitHub', 'https://github.com/surt91'),
    ('Email', 'mailto:hendrik.schawe+web@gmail.com', 'fas fa-envelope'),
    ('Twitter', 'https://twitter.com/surt91'),
    ('Google Scholar', 'https://scholar.google.de/citations?user=-BTuwLgAAAAJ', 'fas fa-graduation-cap'),
    ('Blog', 'https://blog.schawe.me', 'far fa-hand-spock'),
    ('4', None, 'ő'),
    ('857·2²⁴⁶³⁴¹¹+1', None, "'"),
)

DEFAULT_PAGINATION = 3
LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
