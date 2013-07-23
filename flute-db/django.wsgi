import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'flutedb.settings'

sys.path.append('/var/django/flutedb')
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
