#!/usr/bin/python
import sys, os

# Add a custom Python path. (optional)
sys.path.insert(0, "/home/flutedb")

# Switch to the directory of your project.
os.chdir("/home/username/flutedb")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "flutedb.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")