import os


class PathMixin(object):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    VAR_PATH = os.path.join(BASE_DIR, 'var')

    LOGGING_PATH = os.path.join(VAR_PATH, 'log')

    FIXTURE_DIRS = (
        os.path.join(BASE_DIR, '/fixtures/'),
    )

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'var/')
