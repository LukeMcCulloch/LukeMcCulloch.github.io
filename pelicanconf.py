#!/usr/bin/env python
# -*- coding: utf-8 -*- #
#from __future__ import unicode_literals

"""
# instructions:

# https://fedoramagazine.org/make-github-pages-blog-with-pelican/

To publish:
    
cd /Users/lukemcculloch/Documents/projects_git/LukeMcCulloch.github.io-src

make html
make publish
    
cd output
git add .
git commit -m "First post."
git push -u origin master
cd ..
echo '*.pyc' >> .gitignore #don't need pyc files
git add .
git commit -m "First commit."
git push -u origin master


"""

AUTHOR = u'Luke McCulloch'
SITENAME = u'ai, CAD, Optimization-Design and Engineering'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

MARKUP = ('md', 'ipynb')
#PLUGIN_PATHS = ['/media/luke/projects/web/pelican-plugins']   #ELIMINATED: ,'./plugins'       #unecessary
#PLUGIN_PATHS = ['/Users/lukemcculloch/Documents/projects_git/LukeMcCulloch.github.io-src/plugins']
PLUGIN_PATHS = ['/Users/lukemcculloch/Documents/projects_git/pelican-ipynb']
#PLUGINS = ['ipynb.markup',
#           'ipynb.liquid',
#           'liquid_tags',
#           'render_math',
#           'latex']   #ELIMINATED!: 'pelican-ipynb',  #critical

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#src_path = '/media/luke/projects/web/themes'
src_path = '/Users/lukemcculloch/Documents/projects_git/LukeMcCulloch.github.io-src'
src_path = '/Users/lukemcculloch/Documents/projects_git/pelican-themes'
#src_path = '/Users/lukemcculloch/Documents/projects_git/LukeMcCulloch.github.io/theme/css'
#THEME = src_path+'/bootlex'
#THEME = src_path+'/mediumfox' #bad lists!!!  so close.
#THEME = /home/luke/Documents/computational_naval_architecture/projects/themes/mediumfox"
#THEME = src_path+'/Just-Read'  #no
#THEME = src_path+'/chunk'
#THEME = src_path+'/bootstrap'
#THEME = src_path+'/bootstrap2'
THEME = src_path+'/new-bootstrap2'
#THEME = src_path+'/elegant'