from .secret import get_secret

EMAIL_BACKEND = get_secret(section='EMAIL', setting='BACKEND')
EMAIL_HOST = get_secret(section='EMAIL', setting='HOST')
EMAIL_PORT = get_secret(section='EMAIL', setting='PORT')
EMAIL_HOST_USER = get_secret(section='EMAIL', setting='HOST_USER')
EMAIL_HOST_PASSWORD = get_secret(section='EMAIL', setting='HOST_PASSWORD')
EMAIL_USE_TLS = get_secret(section='EMAIL', setting='USE_TLS')
EMAIL_USE_SSL = get_secret(section='EMAIL', setting='USE_SSL')
EMAIL_TIMEOUT = get_secret(section='EMAIL', setting='TIMEOUT')