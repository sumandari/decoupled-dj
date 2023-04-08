from .base import *  # noqa


SECURE_SSL_DIRECT = True
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
STATIC_ROOT = env("STATIC_ROOT")
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

CORS_ALLOW_ALL_ORIGINS = env.list(
   "CORS_ALLOWED_ORIGINS",
   default=[]
)
REST_FRAMEWORK = {
    **REST_FRAMEWORK,
   "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"]
}
