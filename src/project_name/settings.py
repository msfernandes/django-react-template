from decouple import config, Csv
from django.utils.translation import ugettext_lazy as _
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = config('SECRET_KEY', default='secret')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())
ROOT_URLCONF = '{{project_name}}.urls'
WSGI_APPLICATION = '{{project_name}}.wsgi.application'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'compressor',
    'compressor_toolkit',
    'livereload',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'livereload.middleware.LiveReloadScript',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
INTERNAL_IPS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.' + config('DATABASE_ENGINE',
                                                 default='sqlite3'),
        'NAME': config('DATABASE_NAME',
                       default=os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': config('DATABASE_USER', default=''),
        'PASSWORD': config('DATABASE_PASSWORD', default=''),
        'HOST': config('DATABASE_HOST', default=''),
        'PORT': config('DATABASE_PORT', default=''),
    }
}


LOGIN_URL = config('LOGIN_URL', default='/accounts/login/')
LOGIN_REDIRECT_URL = config('LOGIN_REDIRECT_URL', default='/')
LOGOUT_URL = config('LOGOUT_URL', default='/accounts/logout')
LOGOUT_REDIRECT_URL = config('LOGOUT_REDIRECT_URL', default='/')
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'UserAttributeSimilarityValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'MinimumLengthValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'CommonPasswordValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'NumericPasswordValidator'),
    },
]


LANGUAGES = (
    ('pt_BR', _('Português Brasileiro')),
    ('en', _('English')),
)
LANGUAGE_CODE = config('LANGUAGE_CODE', default='pt_BR')
TIME_ZONE = config('TIME_ZONE', default='America/Sao_Paulo')
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]


EMAIL_BACKEND = config('EMAIL_BACKEND',
                       default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False
EMAIL_SUBJECT_PREFIX = ''


# Static files (CSS, JavaScript, Images)
STATIC_URL = config('STATIC_URL', default='/static/')
MEDIA_URL = config('MEDIA_URL', default='/media/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media')
STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (
    ('module', 'compressor_toolkit.precompilers.ES6Compiler'),
    ('text/x-sass', 'compressor_toolkit.precompilers.SCSSCompiler'),
)

COMPRESS_JS_FILTERS = [
    'compressor.filters.yuglify.YUglifyJSFilter',
]

COMPRESS_NODE_MODULES = os.path.join(BASE_DIR, '../node_modules')
COMPRESS_POSTCSS_BIN = os.path.join(BASE_DIR, '../node_modules/.bin/postcss')
COMPRESS_NODE_SASS_BIN = os.path.join(BASE_DIR,
                                      '../node_modules/.bin/node-sass')
COMPRESS_BROWSERIFY_BIN = os.path.join(BASE_DIR,
                                       '../node_modules/.bin/browserify')
COMPRESS_YUGLIFY_BINARY = os.path.join(BASE_DIR,
                                       '../node_modules/.bin/yuglify')
COMPRESS_OFFLINE = config('COMPRESS_OFFLINE', default=False, cast=bool)
