import os

from django.core.wsgi import get_wsgi_application
import configurations

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")


configurations.setup()
application = get_wsgi_application()
