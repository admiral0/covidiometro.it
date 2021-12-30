from split_settings.tools import optional, include
from os import environ

ENV = environ.get('DJANGO_ENV') or 'development'

base_settings = [
    'components/common.py',
    'components/celery.py',
    'components/database.py',
    'components/cache.py',

    'components/gitcoviddi.py',

    f'environments/{ENV}/__init__.py',

    optional('environments/local.py')
]

include(*base_settings)
