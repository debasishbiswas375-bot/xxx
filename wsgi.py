import os
from django.core.wsgi import get_wsgi_application

# IMPORTANT: Ensure 'accountingtools' matches your actual folder name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'accountingtools.settings')

application = get_wsgi_application()
