# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "llllllllllllllllllllllllllllllllllllllllllllllllll"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "example_project.urls"

INSTALLED_APPS = []

INSTALLED_APPS_v3_v4 = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "admin_comments",
    "example"
]

INSTALLED_APPS_v1_10 = [
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django.contrib.auth",
    "django.contrib.sessions",
    "admin_comments",
    "example"
]

if django.VERSION >= (3, 0,):
    INSTALLED_APPS = INSTALLED_APPS_v3_v4

if django.VERSION <= (2, 0,):
    INSTALLED_APPS = INSTALLED_APPS_v1_10

SITE_ID = 1


MIDDLEWARE_v2_v3_v4 = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE_v1_10 = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if django.VERSION >= (1, 10):
    MIDDLEWARE = MIDDLEWARE_v2_v3_v4

if django.VERSION < (1, 10):
    MIDDLEWARE_CLASSES = MIDDLEWARE_v1_10

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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
