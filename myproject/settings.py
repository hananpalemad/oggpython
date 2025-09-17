from pathlib import Path
import os

# -------------------------------------------------
# BASE SETTINGS
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-CHANGE_THIS_TO_A_SECRET_KEY'  # change before production

DEBUG = True  # ✅ turn this OFF (False) on PythonAnywhere for production

# ✅ IMPORTANT: Add your PythonAnywhere domain here
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'yourusername.pythonanywhere.com']


# -------------------------------------------------
# INSTALLED APPS
# -------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ✅ Your app
    'blog',
]

# -------------------------------------------------
# MIDDLEWARE
# -------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------------------------------
# URLS / WSGI
# -------------------------------------------------
ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ✅ global templates folder (optional)
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

WSGI_APPLICATION = 'myproject.wsgi.application'


# -------------------------------------------------
# DATABASE (SQLite by default)
# -------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# -------------------------------------------------
# PASSWORD VALIDATION
# -------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -------------------------------------------------
# LANGUAGE & TIMEZONE
# -------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# -------------------------------------------------
# STATIC FILES (CSS, JS, IMAGES)
# -------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # ✅ for collectstatic on PythonAnywhere
STATICFILES_DIRS = [
    BASE_DIR / "static",  # ✅ if you have a local static/ folder
]

# -------------------------------------------------
# DEFAULT PRIMARY KEY FIELD
# -------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
