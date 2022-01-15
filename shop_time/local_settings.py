SECRET_KEY = '$7(*9y_ot(z4-8lyj=uvx+26$5*my&v-^s(2!r#qi=_fqc6h(7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shop_time',
        'USER': 'postgres',
        'PASSWORD': 'mukyman',
        'HOST': 'localhost'
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'shoptime125@gmail.com'
EMAIL_HOST_PASSWORD = 'mukyman'
EMAIL_USE_TLS = True

BT_ENVIRONMENT = 'sandbox'
BT_MERCHANT_ID = 'gdqpzcdmy9rdfhfg'
BT_PUBLIC_KEY = '9yymyhd7dzs673fz'
BT_PRIVATE_KEY = '083dce5ae12e551084cbec5cc1587aa7'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '225197140918-bsu1vj4cabh3na9a6057ul3qbhq22m04.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'openid'
]
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['first_name', 'last_name']

SOCIAL_AUTH_FACEBOOK_KEY = '896851874358406'
SOCIAL_AUTH_FACEBOOK_SECRET = 'eee634aa329359b2f954cd54d8241749'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'email, first_name, last_name'
}