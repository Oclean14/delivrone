import os
import django
import sys
sys.path.insert(0, "../WebApp_ORM/drone")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
django.setup()

