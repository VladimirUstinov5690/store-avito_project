import sys
import os

# Указываем путь к проекту
sys.path.insert(0, '/home/usinohs/public_html')

# Указываем, какой settings.py использовать
os.environ['DJANGO_SETTINGS_MODULE'] = 'store_wild.settings'

# Импортируем WSGI-приложение Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()