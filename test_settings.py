DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'test.sqlite',
    }
}

INSTALLED_APPS = [
    'nocaptcha',
]

NORECAPTCHA_SECRET_KEY = 'privkey'
NORECAPTCHA_SITE_KEY = 'pubkey'
