from pathlib import Path
import dj_database_url
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ipdoi0j86xchvra0hmi30&^f3v$n9$*z*vec4za2t33sx2+k&6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Modification de ALLOWED_HOSTS pour inclure le domaine Heroku et localhost
ALLOWED_HOSTS = ['olympics-ticketing.fly.dev', 'localhost', '127.0.0.1']


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "reservations",  # Ajout de l'application reservations
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "olympics_ticketing.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # Dossier global des templates
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "olympics_ticketing.wsgi.application"

# Database
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://ue2kr53hl70ctg:p17bb41cca0d2ddc2b2bf52910a5ff9821112a828f508d114f78b705aa3e7560e@c3gtj1dt5vh48j.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d6uhb2678opmv9',
        conn_max_age=600,  # Permet de garder la connexion ouverte pendant 10 minutes
        ssl_require=False   # Nécessite SSL pour la connexion
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "fr-fr"  # Langue par défaut
TIME_ZONE = "Europe/Paris"  # Fuseau horaire

USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Ajout de STATIC_ROOT

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Redirections après connexion/déconnexion
LOGIN_REDIRECT_URL = '/reservations/offres/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# Ajout des domaines de confiance pour la protection CSRF
CSRF_TRUSTED_ORIGINS = ['https://olympics-ticketing.fly.dev']
