"""
Django settings for back project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

import environ
from django.utils.translation import ugettext_lazy as _

env = environ.Env()
environ.Env.read_env(env.str("ENV_PATH", "back/.env"))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

if env("ALLOWED_HOSTS", default="") != "":
    ALLOWED_HOSTS = [host for host in env.list("ALLOWED_HOSTS")]
else:
    # Fallback for old environment variable to avoid breaking change
    ALLOWED_HOSTS = [
        env("ALLOWED_HOST", default="0.0.0.0"),
    ]

if DEBUG:
    ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "users",
    "organization",
    "user_auth",
    "misc",
    "back",
    # admin
    "admin.templates",
    "admin.notes",
    "admin.to_do",
    "admin.resources",
    "admin.introductions",
    "admin.admin_tasks",
    "admin.badges",
    "admin.integrations",
    "admin.preboarding",
    "admin.appointments",
    "admin.sequences",
    "admin.people",
    "admin.settings",
    # new hires
    "new_hire",
    # slack
    "slack_bot",
    # external
    "rest_framework",
    "axes",
    "anymail",
    "django_q",
    "crispy_forms",
]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Login Defaults
LOGIN_REDIRECT_URL = "logged_in_user_redirect"
LOGOUT_REDIRECT_URL = "login"
LOGIN_URL = "login"


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "organization.middleware.HealthCheckMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "users.middleware.language_middleware",
    "axes.middleware.AxesMiddleware",
]

# Django Debug Bar
if DEBUG:
    import socket

    INSTALLED_APPS += [
        "debug_toolbar",
    ]
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
    hostname, _dummy, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]


ROOT_URLCONF = "back.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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
TEMPLATE_DIRS = (os.path.join(BASE_DIR, "templates"),)

WSGI_APPLICATION = "back.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {"default": env.db()}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]


AUTH_USER_MODEL = "users.User"

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication"
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "users.permissions.AdminPermission",
    ],
    "DEFAULT_THROTTLE_RATES": {"anon": "100/day"},
}


# API
if env.bool("API_ACCESS", default=False):
    REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"].append(
        "rest_framework.authentication.TokenAuthentication"
    )
    INSTALLED_APPS += ["rest_framework.authtoken"]

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

if env.bool("MAILGUN", default=False):
    ANYMAIL = {
        "MAILGUN_API_KEY": env("MAILGUN_KEY", default=""),
        "MAILGUN_SENDER_DOMAIN": env("MAILGUN_DOMAIN", default=""),
    }
    EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"

if env.bool("MAILJET", default=False):
    ANYMAIL = {
        "MAILJET_API_KEY": env("MAILJET_API_KEY", default=""),
        "MAILJET_SECRET_KEY": env("MAILJET_SECRET_KEY", default=""),
    }
    EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"

if env.bool("MANDRILL", default=False):
    ANYMAIL = {"MANDRILL_API_KEY": env("MANDRILL_KEY", default="")}
    EMAIL_BACKEND = "anymail.backends.mandrill.EmailBackend"

if env.bool("POSTMARK", default=False):
    ANYMAIL = {"POSTMARK_SERVER_TOKEN": env("POSTMARK_KEY", default="")}
    EMAIL_BACKEND = "anymail.backends.postmark.EmailBackend"

if env.bool("SENDGRID", default=False):
    ANYMAIL = {"SENDGRID_API_KEY": env("SENDGRID_KEY", default="")}
    EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"

if env.bool("SENDINBLUE", default=False):
    ANYMAIL = {"SENDINBLUE_API_KEY": env("SENDINBLUE_KEY", default="")}
    EMAIL_BACKEND = "anymail.backends.sendinblue.EmailBackend"

if env.bool("SPARKPOST", default=False):
    ANYMAIL = {"SPARKPOST_API_KEY": env("SPARKPOST_KEY", default="")}
    EMAIL_BACKEND = "anymail.backends.sparkpost.EmailBackend"

if env.bool("SMTP", default=False):
    EMAIL_HOST = env("EMAIL_HOST", default="localhost")
    EMAIL_PORT = env.int("EMAIL_PORT", default=25)
    EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
    EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
    EMAIL_USE_TLS = env("EMAIL_USE_TLS", default="")
    EMAIL_USE_SSL = env("EMAIL_USE_SSL", default="")
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="example@example.com")

OLD_PASSWORD_FIELD_ENABLED = True

# Caching
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "cached_items",
    }
}

Q_CLUSTER = {
    "name": "DjangORM",
    "workers": 2,
    "timeout": 90,
    "retry": 1800,
    "queue_limit": 50,
    "bulk": 10,
    "orm": "default",
    "catch_up": False,
    "max_attempts": 2,
}

# AWS
AWS_S3_ENDPOINT_URL = env(
    "AWS_S3_ENDPOINT_URL", default="https://s3.eu-west-1.amazonaws.com"
)
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", default="")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", default="")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME", default="")
AWS_REGION = env("AWS_REGION", default="eu-west-1")

if env.str("BASE_URL", "") == "":
    BASE_URL = "https://" + ALLOWED_HOSTS[0]
BASE_URL = env("BASE_URL")

# Twilio
TWILIO_FROM_NUMBER = env("TWILIO_FROM_NUMBER", default="")
TWILIO_ACCOUNT_SID = env("TWILIO_ACCOUNT_SID", default="")
TWILIO_AUTH_TOKEN = env("TWILIO_AUTH_TOKEN", default="")

# Django-Axes
AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    "axes.backends.AxesBackend",
    # Django ModelBackend is the default authentication backend.
    "django.contrib.auth.backends.ModelBackend",
]
AXES_ENABLED = True
AXES_PROXY_ORDER = []
AXES_PROXY_TRUSTED_IPS = []
AXES_PROXY_COUNT = 0
AXES_META_PRECEDENCE_ORDER = [
    "HTTP_X_FORWARDED_FOR",
    "REMOTE_ADDR",
]
AXES_HANDLER = "axes.handlers.database.AxesDatabaseHandler"
AXES_FAILURE_LIMIT = 20
AXES_LOCK_OUT_AT_FAILURE = True
AXES_LOCK_OUT_BY_COMBINATION_USER_AND_IP = False
AXES_ONLY_USER_FAILURES = False
AXES_ONLY_ADMIN_SITE = False
AXES_ENABLE_ADMIN = True
AXES_USE_USER_AGENT = False
AXES_USERNAME_FORM_FIELD = "email"
AXES_PASSWORD_FORM_FIELD = "password"  # noqa
AXES_USERNAME_CALLABLE = None
AXES_WHITELIST_CALLABLE = None
AXES_LOCKOUT_CALLABLE = None
AXES_RESET_ON_SUCCESS = False
AXES_DISABLE_ACCESS_LOG = False
AXES_LOCKOUT_TEMPLATE = None
AXES_LOCKOUT_URL = None
AXES_COOLOFF_TIME = None
AXES_VERBOSE = True
AXES_NEVER_LOCKOUT_WHITELIST = False
AXES_NEVER_LOCKOUT_GET = False
AXES_ONLY_WHITELIST = False
AXES_IP_WHITELIST = None
AXES_IP_BLACKLIST = None
AXES_LOCK_OUT_BY_USER_OR_IP = False
# message to show when locked out and have cooloff enabled
AXES_COOLOFF_MESSAGE = "Account locked: too many login attempts. Please try again later"
AXES_PERMALOCK_MESSAGE = (
    "Account locked: too many login attempts. Contact an admin to unlock your account."
)
PROXY_TRUSTED_IPS = None
REST_FRAMEWORK_ACTIVE = True

# Error tracking
if env.bool("SENTRY", default=False):
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=env("SENTRY_URL", default=""),
        integrations=[
            DjangoIntegration(),
        ],
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=False,
    )

if not env.bool("DEBUG", default=False) and not env.bool(
    "HTTP_INSECURE", default=False
):
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

FIXTURE_DIRS = ["fixtures"]

# Forcing SSL from Django - preferably done a few levels before,
# but this is a last resort in the case of Heroku
if env.bool("SSL_REDIRECT", default=False):
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True

# Storing static files compressed
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# Initial account creation
ACCOUNT_EMAIL = env("ACCOUNT_EMAIL", default="")
ACCOUNT_PASSWORD = env("ACCOUNT_PASSWORD", default="")


# Languages
LANGUAGES = [
    ("en", _("English")),
    ("nl", _("Dutch")),
    ("fr", _("French")),
    ("de", _("German")),
    ("tr", _("Turkish")),
    ("pt", _("Portuguese")),
    ("es", _("Spanish")),
]
LANGUAGE_SESSION_KEY = "chief-language"
SITE_ROOT = os.path.dirname(os.path.realpath(__name__))
LOCALE_PATHS = (os.path.join(SITE_ROOT, "locale"),)
