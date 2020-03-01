import os

from configurations import Configuration

from .apps import AppsMixin
from .path import PathMixin
from .database import DatabaseMixin


class Common(AppsMixin, PathMixin, DatabaseMixin, Configuration):
    @classmethod
    def pre_setup(cls):
        cls.DOTENV = os.path.join(cls.BASE_DIR, '.env')
        super(Common, cls).pre_setup()


class Dev(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = True

    Common.INSTALLED_APPS += [
    ]
