"""
WSGI config for inventory_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""


import os
import sys

# Add your project directory to the sys.path
project_home = '/home/mwizachiwale/inventory'
if project_home not in sys.path:
    sys.path = [inventory_project] + sys.path

# Set the settings module for your Django project
os.environ['DJANGO_SETTINGS_MODULE'] = 'inventory_project.settings'

# Activate the virtual environment
activate_env = '/home/mwizachiwale/venv/bin/activate_this.py'
with open(activate_env) as f:
    exec(f.read(), dict(__file__=activate_env))

# Get the WSGI application for Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
