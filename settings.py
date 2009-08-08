import sys
from os.path import abspath, dirname, join

#put apps dir in the PYTHONPATH
sys.path.insert(0, abspath(join(dirname(__file__), 'apps')))
sys.path.insert(0, abspath(join(dirname(__file__), 'exapps')))

# Django settings for aands project.

from settings_local import *

TIME_ZONE = 'America/Toronto'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = abspath(join(dirname(__file__), 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8SAD0)(*ASDhjfwez^d1%ez4kdtzp0g*4qy6l(-k'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'aands.urls'

TEMPLATE_DIRS = (
    abspath(join(dirname(__file__), 'templates')),
)

INSTALLED_APPS = (
    # django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',
    
    # external apps
    'pagination',
    
    # internal apps
    'core',
    'categories',
    'items',
    'login',
)



