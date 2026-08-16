from pathlib import Path
import os

from decouple import Config, Csv, RepositoryEmpty, RepositoryEnv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Read configuration from a .env file next to the project when present,
# otherwise fall back to real environment variables (e.g. set in the
# PythonAnywhere WSGI file). The .env file is git-ignored.
_env_file = BASE_DIR / ".env"
config = Config(RepositoryEnv(_env_file) if _env_file.is_file() else RepositoryEmpty())


# SECURITY WARNING: keep the secret key used in production secret!
# Set DJANGO_SECRET_KEY in your .env (or environment). The fallback below is
# for local development only and must never be used in production.
SECRET_KEY = config("DJANGO_SECRET_KEY")

print("SECRET_KEY: ", SECRET_KEY)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DJANGO_DEBUG", default=False, cast=bool)

# Comma-separated list of allowed hosts, e.g. DJANGO_ALLOWED_HOSTS="mathedu.pythonanywhere.com"
ALLOWED_HOSTS = config(
    "DJANGO_ALLOWED_HOSTS",
    default="localhost,127.0.0.1,mathedu.pythonanywhere.com",
    cast=Csv(),
)


# Application definition

INSTALLED_APPS = [
    'django.contrib.staticfiles',

    # Third-party apps
    'whitenoise.runserver_nostatic',
    'corsheaders',

    # Local Apps
    'secondary_math',
    'university_math',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'mathedu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates")
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'mathedu.wsgi.application'


# Database
# The application is intentionally stateless: it stores no data, so no
# database is required. Re-enable a database only if you add models
# (e.g. user accounts or saved solution history).


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Logging
# Replace stray print() calls in views with logger.debug/info/error.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{levelname} {asctime} {name} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': config('DJANGO_LOG_LEVEL', default='INFO'),
    },
}