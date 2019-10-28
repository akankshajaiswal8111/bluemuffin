"""
Django settings for awsbluemuffin_project project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f7e#i8(sld-o+012m45$)poag+m=z44n##xo66g@0^s3+4o=2v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['ec2-3-231-57-12.compute-1.amazonaws.com','3.231.57.12','www.bluemuffins.com','172.31.9.16']
ALLOWED_HOSTS = ['bluemuffins.com','172.31.9.16']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'pages',
    'users',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ec2django.urls'

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

WSGI_APPLICATION = 'ec2django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
	'ENGINE': 'django.db.backends.mysql',
	'NAME': 'awsbluemuffin',
	'USER': 'abmadmin',
	'PASSWORD': 'abmadmin123',
	'HOST': 'awsbluemuffin.cna5xveywog4.us-east-1.rds.amazonaws.com',
	'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
AUTH_USER_MODEL = 'users.CustomUser'
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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
#STATIC_URL = '/static/'
#STATIC_ROOT = S3_URL + STATIC_DIRECTORY
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 1

#ACCOUNT_EMAIL_REQUIRED = True
#ACCOUNT_USERNAME_REQUIRED = False
#ACCOUNT_FIRSTNAME_REQUIRED = True
ACCOUNT_FORMS = {'signup':'users.forms.CustomUserCreationForm'}

#AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
#AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
#AWS_ACCESS_KEY_ID =
#AWS_SECRET_ACCESS_KEY = 

#AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
#AWS_STORAGE_BUCKET_NAME =
#AWS_S3_REGION_NAME = 

STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_LOCATION = 'static'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#AWS_S3_FILE_OVERWRITE = False
#AWS_DEFAULT_ACL = 'public-read' 
MEDIAFILES_LOCATION =  'media'
#MEDIA_DIRECTORY = 'media'
#MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, MEDIA_DIRECTORY)
#MEDIA_ROOT = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, MEDIA_DIRECTORY)
#MEDIA_URL = '/media/'

DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        )
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
CDN_DOMAIN = 'dihhaoyfz46p4.cloudfront.net'

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#S3_URL = 'http://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
#STATIC_DIRECTORY = '/static/'
#MEDIA_DIRECTORY = '/media/'
#STATIC_URL = S3_URL + STATIC_DIRECTORY
#STATIC_ROOT = S3_URL + STATIC_DIRECTORY
#MEDIA_URL = S3_URL + MEDIA_DIRECTORY
MAX_UPLOAD_SIZE = 10485760
