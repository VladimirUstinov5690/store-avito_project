import sys
import os

# Указываем путь к проекту
sys.path.insert(0, '/var/www/avitostat')
sys.path.insert(1, '/var/www/avitostat/venv/lib/python3.12/site-packages/django/__init__.py')

# Указываем, какой settings.py использовать
os.environ['DJANGO_SETTINGS_MODULE'] = 'store_wild.settings'

# Импортируем WSGI-приложение Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()