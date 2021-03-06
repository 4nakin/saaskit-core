# This module is available as common_settings from projects' settings module.
# It contains settings used in all projects.

import os.path
from django.conf import global_settings

KIT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True 
TEMPLATE_DEBUG = DEBUG
DEBUG_PROPAGATE_EXCEPTIONS = False

ADMINS = (
     ('SaaSkit', 'admin@saaskit.org'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'  			         # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(KIT_ROOT, 'saaskit.db')     # Or path to database file if using sqlite3.
DATABASE_USER = '' 			            	 # Not used with sqlite3.
DATABASE_PASSWORD = ''         				 # Not used with sqlite3.
DATABASE_HOST = ''             				 # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             				 # Set to empty string for default. Not used with sqlite3.

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',         # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME':  os.path.join(KIT_ROOT, 'saaskit.db'),	# Or path to database file if using sqlite3.
#        'USER': '',                         		# Not used with sqlite3.
#        'PASSWORD': '',                 		# Not used with sqlite3.
#        'HOST': '',                             	# Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '',                         		# Set to empty string for default. Not used with sqlite3.
#    }
#}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(KIT_ROOT, 'site_media')
APP_MEDIA_ROOT = MEDIA_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

SERVE_MEDIA = True

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'sso.middleware.SingleSignOnMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'subscription.middleware.SubscriptionMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'sso.middleware.SingleSignOnMiddleware',
    'muaccount_content.middleware.FlatpageFallbackMiddleware',
    'django_error_capture_middleware.ErrorCaptureMiddleware',
    'wurfl.middleware.DeviceMiddleware',
)

ROOT_URLCONF = 'saaskit.urls'

INSTALLED_APPS = (
    'saaskit',
                  
    # builtin
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    
    'compress',
    'contact',
    'emailconfirmation',
    'registration',
    'django_extensions',
    'django_pipes',
    'notification',
    'paypal.standard.ipn',
    'profiles',
    'sorl.thumbnail',
    'south',
    'sso',
    'tagging',
    'oembed',
    'templatesadmin',
    'uni_form',
    'pagination',
    'app_media',
    'friends',
    'tinymce',
    'frontendadmin',
    'django_counter',
    'rosetta',
    'django_error_capture_middleware',    
    'wurfl',

    # own
    'muaccounts',
    'prepaid',
    'quotas',
    'subscription',
    
    # local
    'saaskit_profile',
    'muaccount_content',
    'muaccount_adsense',
    'muaccounts_quotas',
    'page_view_quotas',
    
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    )
TEMPLATE_DIRS = ( os.path.join(KIT_ROOT, 'templates').replace('\\','/'), )

TEST_RUNNER = "saaskit.tests.coverage_runner.run_tests"
COVERAGE_REPORT_PATH = os.path.join(KIT_ROOT, 'coverage_report')

AUTHENTICATION_BACKENDS = ('subscription.backends.UserSubscriptionBackend',)

# Settings for templates editing via django admin

TEMPLATESADMIN_HIDE_READONLY = True
TEMPLATESADMIN_GROUP = 'Editors'
TEMPLATESADMIN_VALID_FILE_EXTENSIONS = (
        'html',
        'css',
        'txt',
        'backup',
   )

TEMPLATESADMIN_EDITHOOKS = (
         'templatesadmin.edithooks.dotbackupfiles.DotBackupFilesHook',
#        'templatesadmin.edithooks.gitcommit.GitCommitHook',
   )

import user_site

TEMPLATESADMIN_TEMPLATE_DIRS = (
      os.path.join(os.path.dirname(user_site.__file__), 'templates').replace('\\','/'),
   ) + TEMPLATE_DIRS

INTERNAL_IPS = ( '127.0.0.1', )

AUTH_PROFILE_MODULE = 'saaskit_profile.UserProfile'

SSO_SECRET = "6O4nVw|~w't2mxV%oeSUDew{9zhN.\"lY1T.xi9nmZL+lNxGlr@K5+~>NnLMHNAN]57s"

ERROR_CAPTURE_ENABLE_MULTPROCESS = True
ERROR_CAPTURE_HANDLERS = (
    'django_error_capture_middleware.handlers.github.GitHubHandler',
)

# regular expressions to block
#ERROR_CAPTURE_TRACE_CONTENT_BLACKLIST = (
#)

# (ACTUAL) classes to blacklist
#ERROR_CAPTURE_TRACE_CLASS_BLACKLIST = (
#)

ERROR_CAPTURE_GITHUB_REPO = 'saas-kit/saaskit-core'
ERROR_CAPTURE_GITHUB_TOKEN = 'fdb2f708d1a7b8be999771d037d401cc'
ERROR_CAPTURE_GITHUB_LOGIN = 'saas-kit'

ERROR_CAPTURE_NOOP_ON_DEBUG = False

SERVER_EMAIL = 'admin@saaskit.org'
ERROR_CAPTURE_EMAIL_FAIL_SILENTLY = False
ERROR_CAPTURE_IGNORE_DUPE_SEC = False 

COMPRESS = False
COMPRESS_VERSION = False

_default_css_files = ('uni_form/uni_form/uni-form-generic.css',
                      'uni_form/uni_form/uni-form.css',
                      'saaskit/css/saaskit.css',
                      )

_default_js_files = ('saaskit/js/openid-jquery.js',
                     'uni_form/uni_form/uni-form.jquery.js',
                     'saaskit/js/saaskit.js',
                    )

COMPRESS_CSS = {      
    'all' : {
        'name' : 'Default theme',
        'source_filenames' : _default_css_files,
        'output_filename' : 'style.css'},
    }

COMPRESS_JS = {
    'all' : {
        'source_filenames' : _default_js_files, 
        'output_filename' : 'scripts.js'},
    }

ACCOUNT_ACTIVATION_DAYS=7
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/'

SSO_URL = '/sso/'
LOGOUT_URL = '/accounts/logout/'


QUOTAS = {
    'muaccount_members' : (3, 10, 50),
    'muaccounts': (1, 5),
    'page_views': (10000, 10000000),
    }

GRACE_PAGE_VIEW = 1000

MUACCOUNTS_ROOT_DOMAIN = 'example.com'
MUACCOUNTS_DEFAULT_URL = 'http://www.example.com:8001/'
MAIN_SITE_PORT = 8001
MUACCOUNTS_PORT = 8000

MUACCOUNTS_IP = '127.0.0.1'
MUACCOUNTS_MAIN_URLCONF = 'main_site.urls'
MUACCOUNTS_USERSITE_URLCONF = 'user_site.urls'
MUACCOUNTS_SUBDOMAIN_STOPWORDS = (r"^www$", r"^support$", r"^lab$", r"^labs$", r"^dev$", r"^development$", r"^ops$", r"^operations$", r"^corp$", r"^media$", r"^assets$", r"^mail$", r"^docs$", r"^calendar$", r"^contacts$", r"^feedback$", r"^chat$")
MUACCOUNTS_THEMES = (
    # color css
    ('color_scheme', 'Color scheme', (
        ('aqua', 'Aqua', 'saaskit/themes/aqua.css'),
        ('green', 'Green', 'saaskit/themes/green.css'),
        ('purple', 'Purple', 'saaskit/themes/purple.css'),
        ('red', 'Red', 'saaskit/themes/red.css'),
        ('tan-blue', 'Tan Blue', 'saaskit/themes/tan_blue.css'),
        )),
    # <body> id
    ('page_width', 'Page widgh', (
        ('doc3', '100% fluid'),
        ('doc', '750px centered'),
        ('doc2', '950px centered'),
        ('doc4', '974px fluid'),
        )),
    # Outermost <div> class
    ('layout', 'Layout', (
        ('yui-t6', 'Right sidebar, 300px'),
        ('yui-t1', 'Left sidebar, 160px'),
        ('yui-t2', 'Left sidebar, 180px'),
        ('yui-t3', 'Left sidebar, 300px'),
        ('yui-t4', 'Right sidebar, 180px'),
        ('yui-t5', 'Right sidebar, 240px'),
        ('yui-t0', 'Single Column'),
        )),
    # <body> class
    ('rounded_corners', 'Rounded corners', (
        ('on', 'On', 'rounded'),
        ('off', 'Off', ''),
        )),
    )

ROOT_URL = MUACCOUNTS_DEFAULT_URL
PREPAID_DEFAULT_EXPIRY_PERIOD = 31

ugettext = lambda s: s

LANGUAGES = (
    ('en', ugettext('English')),
    ('de', ugettext('German')),
    ('fr', ugettext('French')),
    ('ru', ugettext('Russian')),
    ('sv', ugettext('Swedish')),
)

# Prepare CSS files for configured color schemes
for codename, _, css_file in MUACCOUNTS_THEMES[0][2]:
     COMPRESS_CSS[codename] = {
         'source_filenames' : ( _default_css_files + (css_file,)
                                ),
         'output_filename' : 'style.%s.css' % codename,
         }

SITE_NAME = 'SaaSkit'
DEFAULT_FROM_EMAIL = 'support@example.com'
CONTACT_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_SUBJECT_PREFIX = "[SaaSKit] "
EMAIL_CONFIRMATION_DAYS = 2

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced", 'relative_urls': True, 
    'height': '700px', 'width': '79%', 
    'theme_advanced_toolbar_location' : "top",
}
TINYMCE_JS_ROOT = os.path.join(MEDIA_ROOT, 'saaskit/js/tiny_mce')

PAYPAL_PRO = False

#Dummy paypal settings
PAYPAL_TEST = True
PAYPAL_RECEIVER_EMAIL='admin_1259179300_biz@crowdsense.com'
SUBSCRIPTION_PAYPAL_SETTINGS = {
    'business' : PAYPAL_RECEIVER_EMAIL,
    }

# Website payments Pro settings
PAYPAL_WPP_USER = ""
PAYPAL_WPP_PASSWORD = ""
PAYPAL_WPP_SIGNATURE = ""

# Prepaid Settings

PREPAID_ITEM_PREFIX = 'P'
PREPAID_UNIT_COST = '1'
PREPAID_MIN_WITHDRAWAL = '20'
PREPAID_AUTO_APPROVE_WITHDRAWALS = 'True'
ROOT_URL = 'http://example.com:8001/'

RECHARGE_TEXT = 'Point Purchase'

PREPAID_UNIT_PACKS = (
	(10, '1.29'),
	(100, '12.49'),
	(250, '29.99'),
	(500, '57.99'),
	(1000, '109.99'),
)

# Local settings for development / production
try:
     from local_settings import *
except ImportError:
     pass

if PAYPAL_PRO:
    INSTALLED_APPS += ('paypal.standard', 'paypal.pro')

TINYMCE_JS_URL = '%s/saaskit/js/tiny_mce/tiny_mce.js' % MEDIA_URL
