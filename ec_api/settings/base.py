import contextlib
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys

import dc_design_system
from django.urls.base import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))


def here(*path):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *path)


PROJECT_ROOT = here("..")


def root(*path):
    return os.path.join(os.path.abspath(PROJECT_ROOT), *path)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "frontend",
    "pipeline",
    "dc_design_system",
    "users",
    "api_docs",
    "apiblueprint_view",
    "debug_toolbar",
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ec_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "ec_api.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
domain = os.environ.get("APP_DOMAIN")
DEFAULT_FROM_EMAIL = f"no-reply@{domain}"

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = "users.CustomUser"

LOGIN_URL = reverse_lazy("users:login")

# django-sesame settings
AUTHENTICATION_BACKENDS = ["sesame.backends.ModelBackend"]
SESAME_MAX_AGE = 60 * 10
SESAME_ONE_TIME = True
SESAME_TOKEN_NAME = "login_token"

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    "GET",
    "OPTIONS",
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-GB"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = (root("assets"),)
STATIC_ROOT = root("static")

STORAGES = {
    "staticfiles": {"BACKEND": "pipeline.storage.PipelineManifestStorage"}
}

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "pipeline.finders.PipelineFinder",
    "pipeline.finders.CachedFileFinder",
)

PIPELINE = {
    "COMPILERS": ("pipeline.compilers.sass.SASSCompiler",),
    "SASS_BINARY": "pysassc",
    "CSS_COMPRESSOR": "pipeline.compressors.NoopCompressor",
    "STYLESHEETS": {
        "styles": {
            "source_filenames": ("scss/styles.scss",),
            "output_filename": "css/styles.css",
            "extra_context": {
                "media": "screen,projection",
            },
        },
    },
    "JAVASCRIPT": {
        "mermaid": {
            "source_filenames": ("js/mermaid.js",),
            "output_filename": "mermaid.js",
        }
    },
}

PIPELINE["SASS_ARGUMENTS"] = (
    " -I " + dc_design_system.DC_SYSTEM_PATH + "/system"
)

PIPELINE["CSS_COMPRESSOR"] = "pipeline.compressors.NoopCompressor"
PIPELINE["JS_COMPRESSOR"] = "pipeline.compressors.NoopCompressor"

WIDGET_S3_URL = os.environ.get(
    "WIDGET_S3_URL",
    "https://ec-api-staging-widget.s3.eu-west-2.amazonaws.com/widget.js",
)


def setup_sentry(environment=None):
    SENTRY_DSN = os.environ.get("SENTRY_DSN")
    if not SENTRY_DSN:
        return

    if not environment:
        environment = os.environ["SAM_LAMBDA_CONFIG_ENV"]
    release = os.environ.get("GIT_HASH", "unknown")
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        traces_sample_rate=None,
        environment=environment,
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
        release=release,
    )


DC_API_URL = "https://developers.democracyclub.org.uk"
DC_API_TOKEN = "changeme"


# Lambda: https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-runtime
# CircleCI: https://circleci.com/docs/2.0/env-vars/#built-in-environment-variables
# Make: https://docs.oracle.com/cd/E19504-01/802-5880/makeattapp-21/index.html


def is_local_dev():
    vars_to_check = ["AWS_LAMBDA_FUNCTION_NAME", "CI", "MAKEFLAGS"]
    return not any(ev in os.environ for ev in vars_to_check)


# .local.py overrides all the common settings.
if is_local_dev():
    with contextlib.suppress(ImportError):
        from .local import *  # noqa


def is_running_tests():
    if os.environ.get("RUN_ENV") == "test":
        return True
    if "CI" in os.environ:
        return True
    return False


if is_running_tests():
    with contextlib.suppress(ImportError):
        from .testing import *  # noqa
