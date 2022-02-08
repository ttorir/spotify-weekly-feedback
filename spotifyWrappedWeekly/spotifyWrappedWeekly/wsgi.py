"""
WSGI config for spotifyWrappedWeekly project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotifyWrappedWeekly.settings')

#application = get_wsgi_application()


#application = DjangoWhiteNoise(application)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prompt.settings")

#from whitenoise.django import DjangoWhiteNoise

application = WhiteNoise(get_wsgi_application())