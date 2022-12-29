import os
from .common import Common
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Common):
    DEBUG = True

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += ('django_nose', "debug_toolbar",
                       )
    MIDDLEWARE = Common.MIDDLEWARE
    MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",

                   )
    SECRET_KEY = Common.SECRET_KEY
    SECRET_KEY = 'ju^&8@6obov+sri544qm+t0wx-^dp5cmc8l*5w*wo^j)(!7+x('
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    NOSE_ARGS = [
        BASE_DIR,
        '-s',
        '--nologcapture',
        '--with-coverage',
        '--with-progressive',
        '--cover-package=todo'
    ]

    # Mail
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    INTERNAL_IPS = [
        # ...
        "127.0.0.1",
        # ...
    ]
