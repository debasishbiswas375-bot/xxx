import os
from django.core.wsgi import get_wsgi_application

# Points to 'accountingtools/settings.py'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'accountingtools.settings')

application = get_wsgi_application()
