"""
Django settings for ddrlocal project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# ----------------------------------------------------------------------

DEBUG = True
TEMPLATE_DEBUG = DEBUG

import ConfigParser
from datetime import timedelta
import logging
import sys

import pytz

os.environ['USER'] = 'ddr'

AGENT = 'ddr-local'

from DDR.config import CONFIG_FILES, NoConfigError
config = ConfigParser.ConfigParser()
configs_read = config.read(CONFIG_FILES)
if not configs_read:
    raise NoConfigError('No config file!')

REPO_MODELS_PATH = config.get('cmdln','repo_models_path')
if REPO_MODELS_PATH not in sys.path:
    sys.path.append(REPO_MODELS_PATH)

# Latest commits for ddr-cmdln and ddr-local.
# Include here in settings so only has to be retrieved once,
# and so commits are visible in error pages and in page footers.
from DDR import dvcs
DDRCMDLN_INSTALL_PATH = config.get('cmdln','install_path')
DDRCMDLN_COMMIT = dvcs.latest_commit(DDRCMDLN_INSTALL_PATH)
DDRLOCAL_COMMIT = dvcs.latest_commit(os.path.dirname(__file__))

# The following settings are in debian/config/ddr.cfg.
# See that file for comments on the settings.
# ddr.cfg is installed in /etc/ddr/ddr.cfg.
# Settings in /etc/ddr/ddr.cfg may be overridden in /etc/ddr/local.cfg.

GITOLITE             = config.get('workbench','gitolite')
GITOLITE_TIMEOUT     = config.get('workbench','gitolite_timeout')
CGIT_URL             = config.get('workbench','cgit_url')
GIT_REMOTE_NAME      = config.get('workbench','remote')
IDSERVICE_API_BASE   = config.get('idservice','api_base')

MEDIA_BASE           = config.get('cmdln','media_base')
# Location of Repository 'ddr' repo, which should contain repo_models
# for the Repository.

# see notes in ddrlocal.cfg
try:
    DEFAULT_TIMEZONE = config.get('cmdln','default_timezone')
except:
    DEFAULT_TIMEZONE = 'America/Los_Angeles'
TZ = pytz.timezone(DEFAULT_TIMEZONE)
DATETIME_FORMAT = config.get('cmdln','datetime_format')
DATE_FORMAT = config.get('cmdln','date_format')
TIME_FORMAT = config.get('cmdln','time_format')
PRETTY_DATETIME_FORMAT = config.get('cmdln','pretty_datetime_format')
PRETTY_DATE_FORMAT = config.get('cmdln','pretty_date_format')
PRETTY_TIME_FORMAT = config.get('cmdln','pretty_time_format')

TEMPLATE_CJSON       = config.get('cmdln','template_cjson')
TEMPLATE_EJSON       = config.get('cmdln','template_ejson')
TEMPLATE_EAD         = os.path.join(REPO_MODELS_PATH, 'templates', 'ead.xml')
TEMPLATE_METS        = os.path.join(REPO_MODELS_PATH, 'templates', 'mets.xml')
ACCESS_FILE_APPEND   = config.get('cmdln','access_file_append')
ACCESS_FILE_EXTENSION = config.get('cmdln','access_file_extension')
ACCESS_FILE_GEOMETRY = config.get('cmdln','access_file_geometry')
ACCESS_FILE_OPTIONS  = config.get('cmdln','access_file_options')
THUMBNAIL_GEOMETRY   = config.get('cmdln','thumbnail_geometry')
THUMBNAIL_COLORSPACE = 'sRGB'
THUMBNAIL_OPTIONS    = config.get('cmdln','thumbnail_options')

GITWEB_URL           = config.get('local','gitweb_url')
SUPERVISORD_URL      = config.get('local','supervisord_url')
SUPERVISORD_PROCS    = ['ddrlocal', 'celery']
MUNIN_URL            = config.get('local','munin_url')
SECRET_KEY           = config.get('local','secret_key')
LANGUAGE_CODE        = config.get('local','language_code')
TIME_ZONE            = config.get('local','time_zone')
VIRTUALBOX_SHARED_FOLDER = config.get('local','virtualbox_shared_folder')
DDR_ORGANIZATIONS    = config.get('local','organizations').split(',')
DDR_SSHPUB_PATH      = config.get('local','ssh_pubkey')
DDR_PROTOTYPE_USER   = config.get('testing','user_name')
DDR_PROTOTYPE_MAIL   = config.get('testing','user_mail')
STATIC_ROOT          = config.get('local','static_root')
STATIC_URL           = config.get('local','static_url')
MEDIA_ROOT           = config.get('local','media_root')
MEDIA_URL            = config.get('local','media_url')
DEFAULT_PERMISSION_COLLECTION = config.get('local','default_permission_collection')
DEFAULT_PERMISSION_ENTITY     = config.get('local','default_permission_entity')
DEFAULT_PERMISSION_FILE       = config.get('local','default_permission_file')
LOG_DIR              = config.get('local', 'log_dir')
LOG_FILE             = config.get('local', 'log_file')
LOG_LEVEL            = config.get('local', 'log_level')
VOCAB_TERMS_URL      = config.get('local', 'vocab_terms_url')
CSV_EXPORT_PATH = {
    'entity': '/tmp/ddr/csv/%s-objects.csv',
    'file': '/tmp/ddr/csv/%s-files.csv',
}

# ElasticSearch
DOCSTORE_INDEX       = config.get('local', 'docstore_index')
ds_host,ds_port      = config.get('local', 'docstore_host').split(':')
DOCSTORE_HOSTS = [
    {'host':ds_host, 'port':ds_port}
]
RESULTS_PER_PAGE = 20

GITOLITE_INFO_CACHE_TIMEOUT = int(config.get('local', 'gitolite_info_cache_timeout'))
GITOLITE_INFO_CACHE_CUTOFF  = int(config.get('local', 'gitolite_info_cache_cutoff'))
GITOLITE_INFO_CHECK_PERIOD  = int(config.get('local', 'gitolite_info_check_period'))

TESTING_USERNAME     = config.get('testing','username')
TESTING_PASSWORD     = config.get('testing','password')
TESTING_REPO         = config.get('testing','repo')
TESTING_ORG          = config.get('testing','org')
TESTING_CID          = config.get('testing','cid')
TESTING_EID          = config.get('testing','eid')
TESTING_ROLE         = config.get('testing','role')
TESTING_SHA1         = config.get('testing','sha1')
TESTING_DRIVE_LABEL  = config.get('testing','drive_label')
TESTING_CREATE       = int(config.get('testing','create'))

# Directory in root of USB HDD that marks it as a DDR disk
# /media/USBHDDNAME/ddr
DDR_USBHDD_BASE_DIR = 'ddr'

ENTITY_FILE_ROLES = (
    ('master','master'),
    ('mezzanine','mezzanine'),
    ('access','access'),
)

# Django uses a slightly different datetime format
DATETIME_FORMAT_FORM = '%Y-%m-%d %H:%M:%S'

# cache key used for storing URL of page user was requesting
# when redirected to either login or storage remount page
REDIRECT_URL_SESSION_KEY = 'remount_redirect_uri'

REPOS_ORGS_TIMEOUT = 60*30 # 30min

GITSTATUS_LOG = '/var/log/ddr/gitstatus.log'
# File used to manage queue for gitstatus-update
GITSTATUS_QUEUE_PATH = os.path.join(MEDIA_BASE, '.gitstatus-queue')
# Processes that should not be interrupted by gitstatus-update should
# write something to this file (doesn't matter what) and remove the file
# when they are finished.
GITSTATUS_LOCK_PATH = os.path.join(MEDIA_BASE, '.gitstatus-stop')
# Normally a global lockfile allows only a single gitstatus process at a time.
# To allow multiple processes (e.g. multiple VMs using a shared storage device),
# add the following setting to /etc/ddr/local.cfg:
#     gitstatus_use_global_lock=0
GITSTATUS_USE_GLOBAL_LOCK = True
if config.has_option('local', 'gitstatus_use_global_lock'):
    GITSTATUS_USE_GLOBAL_LOCK = config.get('local', 'gitstatus_use_global_lock')
# Minimum interval between git-status updates per collection repository.
GITSTATUS_INTERVAL = 60*60*1
GITSTATUS_BACKOFF = 30
# Indicates whether or not gitstatus_update_store periodic task is active.
# This should be True for most single-user workstations.
# See CELERYBEAT_SCHEDULE below.
# IMPORTANT: If disabling GITSTATUS, also remove the celerybeat config file
# and restart supervisord:
#   $ sudo supervisorctl stop celerybeat
#   $ sudo rm /etc/supervisor/conf.d/celerybeat.conf
#   $ sudo supervisorctl reload
GITSTATUS_BACKGROUND_ACTIVE = True
if config.has_option('local', 'gitstatus_background_active'):
    GITSTATUS_BACKGROUND_ACTIVE = config.get('local', 'gitstatus_background_active')
    SUPERVISORD_PROCS.append('celerybeat')

MANUAL_URL = os.path.join(MEDIA_URL, 'manual')

# ----------------------------------------------------------------------

import djcelery
djcelery.setup_loader()

ADMINS = (
    ('geoffrey jost', 'geoffrey.jost@densho.org'),
    #('Geoff Froh', 'geoff.froh@densho.org'),
)
MANAGERS = ADMINS

SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #
    'bootstrap_pagination',
    'djcelery',
    'gunicorn',
    'sorl.thumbnail',
    #
    'ddrlocal',
    'storage',
    'webui',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/lib/ddr/ddrlocal.db',
    }
}

REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'
REDIS_DB_CACHE = 0
REDIS_DB_CELERY_BROKER = 1
REDIS_DB_CELERY_RESULT = 2
REDIS_DB_SORL = 3

CACHES = {
    "default": {
        "BACKEND": "redis_cache.cache.RedisCache",
        "LOCATION": "%s:%s:%s" % (REDIS_HOST, REDIS_PORT, REDIS_DB_CACHE),
        "OPTIONS": {
            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
        }
    }
}

# celery
CELERY_TASKS_SESSION_KEY = 'celery-tasks'
CELERY_RESULT_BACKEND = 'redis://%s:%s/%s' % (REDIS_HOST, REDIS_PORT, REDIS_DB_CELERY_RESULT)
BROKER_URL            = 'redis://%s:%s/%s' % (REDIS_HOST, REDIS_PORT, REDIS_DB_CELERY_BROKER)
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 60 * 60}  # 1 hour
CELERYD_HIJACK_ROOT_LOGGER = False
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
CELERYBEAT_SCHEDULER = None
CELERYBEAT_PIDFILE = None
CELERYBEAT_SCHEDULE = {
    'webui-gitolite-info-refresh': {
        'task': 'webui.tasks.gitolite_info_refresh',
        'schedule': timedelta(seconds=GITOLITE_INFO_CHECK_PERIOD),
    }
}
if GITSTATUS_BACKGROUND_ACTIVE:
    CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
    CELERYBEAT_PIDFILE = '/tmp/celerybeat.pid'
    CELERYBEAT_SCHEDULE['webui-git-status-update-store'] = {
        'task': 'webui.tasks.gitstatus_update_store',
        'schedule': timedelta(seconds=60),
    }

# sorl-thumbnail
THUMBNAIL_DEBUG = DEBUG
#THUMBNAIL_DEBUG = False
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
#THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.cached_db_kvstore.KVStore'
THUMBNAIL_REDIS_PASSWORD = ''
THUMBNAIL_REDIS_HOST = REDIS_HOST
THUMBNAIL_REDIS_PORT = int(REDIS_PORT)
THUMBNAIL_REDIS_DB = REDIS_DB_SORL
THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.convert_engine.Engine'
THUMBNAIL_CONVERT = 'convert'
THUMBNAIL_IDENTIFY = 'identify'
THUMBNAIL_CACHE_TIMEOUT = 60*60*24*365*10  # 10 years

SESSION_ENGINE = 'redis_sessions.session'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
    '/usr/local/src/ddr-local/ddrlocal/ddrlocal/templates',
    '/usr/local/src/ddr-local/ddrlocal/storage/templates',
    '/usr/local/src/ddr-local/ddrlocal/webui/templates',
)

STATICFILES_DIRS = (
    #'/opt/ddr-local/ddrlocal/ddrlocal/static',
    #'/usr/local/src/ddr-local/ddrlocal/storage/static',
    '/usr/local/src/ddr-local/ddrlocal/webui/static',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)-8s [%(module)s.%(funcName)s]  %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)-8s %(message)s'
        },
    },
    'filters': {
        # only log when settings.DEBUG == False
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'suppress_celery_newconnect': {
            '()': 'webui.log.SuppressCeleryNewConnections'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': LOG_FILE,
            'when': 'D',
            'backupCount': 14,
            'filters': ['suppress_celery_newconnect'],
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'level': 'ERROR',
            'propagate': True,
            'handlers': ['mail_admins'],
        },
    },
    # This is the only way I found to write log entries from the whole DDR stack.
    'root': {
        'level': 'DEBUG',
        'handlers': ['file'],
    },
}

USE_TZ = True
USE_I18N = True
USE_L10N = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'storage.context_processors.sitewide',
    'webui.context_processors.sitewide',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ddrlocal.urls'

WSGI_APPLICATION = 'ddrlocal.wsgi.application'
