import os
# from decouple import config
from dj_database_url import parse as dburl

# import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/


ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'dal' ,
    'dal_select2' ,
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'core',
    'loja',
    'bootstrap4',
    'multiselectfield',
    'crispy_forms',
    'localflavor',
    'django_extensions',
    # Autenticação com Redes Sociais
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.twitter',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'locadora.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "core", "templates"), os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, "loja", "templates")],
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

WSGI_APPLICATION = 'locadora.wsgi.application'

AUTH_USER_MODEL = 'core.User'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


DECIMAL_SEPARATOR = ','
USE_THOUSAND_SEPARATOR = True

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

BOOTSTRAP4 = {
    # The URL to the jQuery JavaScript file
    'jquery_url': os.path.join(STATIC_URL, 'vendor/jquery/jquery.min.js'),

    # The Bootstrap base URL
    'base_url': os.path.join(STATIC_URL, 'static/'),

    # The complete URL to the Bootstrap CSS file (None means derive it from base_url)
    'css_url': os.path.join(STATIC_URL, 'vendor/bootstrap/css/bootstrap.min.css'),

    # The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
    'javascript_url': os.path.join(STATIC_URL, 'vendor/bootstrap/js/bootstrap.min.js'),

}

# DATABASE_URL="postgres://mwlsmycgybaqap:521876ffb44ac01bd33b94a0036017efb82eb62b78fa1a4484b8ff0ada8ddf1e@ec2-54-225-227-125.compute-1.amazonaws.com:5432/dfkp1nm6mi0iov"
# logging
# django_heroku.settings(locals())

#Crispy Form

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'core:redireciona-usuario'
LOGOUT_REDIRECT_URL = 'index'

# `allauth`
SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_FORMS = {'login': 'core.forms.MyLoginForm'}

# Configuração de E-mail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'postmaster@mg.locadora-cin.com'
EMAIL_HOST_PASSWORD = '0acb5347d07a2855b7c6ad0c6ee90afb-b9c15f4c-f973d66a'
EMAIL_USE_TLS = True
