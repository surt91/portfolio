#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hendrik Schawe'
SITENAME = 'Hendrik Schawe'
# SITESUBTITLE = 'lorem ipsum dolor sit amet'
SITEURL = 'https://hendrik.schawe.me'

PUBLICATIONS = [
    {
        "doi": "10.1209/0295-5075/113/30004",
        "arxiv": "1512.08554",
        "pdf": "2016_TSP_EPL.pdf",
    },
    {
        "doi": "10.1038/s41598-017-08531-8",
        "pdf": "2017_IFM_SciRep.pdf",
    },
    {
        "doi": "10.1103/PhysRevE.96.062101",
        "arxiv": "1709.02638",
        "pdf": "2017_convex_highdim_PRE.pdf",
    },
    {
        "doi": "10.1103/PhysRevE.97.062159",
        "arxiv": "1804.02371",
        "pdf": "2018_convex_avoiding_PRE.pdf",
    },
    {
        "doi": "10.1209/0295-5075/124/40005",
        "arxiv": "1808.09246",
        "pdf": "2018_srn_EPL.pdf",
    },
    {
        "doi": "10.1103/PhysRevE.99.042104",
        "arxiv": "1901.05235",
        "pdf": "2019_lis_PRE.pdf",
    },
    {
        "doi": "10.1140/epjb/e2019-90667-y",
        "arxiv": "1811.04816",
        "pdf": "2019_bi_EPJB_accepted.pdf",
    },
    {
        "doi": "10.1371/journal.pone.0215309",
        "arxiv": "1702.02821",
        "pdf": "2019_sat_PLOSONE.pdf",
    },
]

PREPRINTS = [
    {
        "arxiv": "1808.10698",
        "pdf": "pp_true",
    },
    {
        "arxiv": "1806.08681",
        "pdf": "pp_tsprsb",
    },
    {
        "arxiv": "1803.08015",
        "pdf": "pp_bat",
    },
    {
        "arxiv": "1907.00486",
        "pdf": "pp_pp_lis2",
    },
]

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
    "render_math",
    "sitemap",
    "preload_thumbnail",
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
    'extra/service-worker-registration.js',
    'extra/service-worker-registration.min.js',
    'extra/custom.css',
    'extra/favicon.ico',
    'extra/icons',
    'theme/images',
    'extra/googlee1eadb2ddedaa639.html',
    'extra/BingSiteAuth.xml',
    'img',
    'pdf',
]

EXTRA_PATH_METADATA = {
    'extra/manifest.json': {'path': 'manifest.json'},
    'extra/custom.css': {'path': 'custom.css'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/googlee1eadb2ddedaa639.html': {'path': 'googlee1eadb2ddedaa639.html'},
    'extra/BingSiteAuth.xml': {'path': 'BingSiteAuth.xml'},
}

SITE_DESCRIPTION = 'Hendrik Schawe'
FEATURED_IMAGE = 'https://blog.schawe.me/img/logo.png'

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
    ('Email', 'mailto:hendrik.schawe+web@gmail.com', 'envelope'),
    ('Twitter', 'https://twitter.com/surt91'),
    ('Google Scholar', 'https://scholar.google.de/citations?user=-BTuwLgAAAAJ', 'graduation-cap'),
    ('Blog', 'https://blog.schawe.me', 'hand-spock-o'),
    ('4', None, 'ő'),
    ('857·2²⁴⁶³⁴¹¹+1', None, "'"),
)

DEFAULT_PAGINATION = 3
LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
