from decouple import config

environment = config("DJANGO_ENV", "TEST")

if environment == "LOCAL":
    from .local import *
if environment == "TEST":
    from .test import *
if environment == "PRODUCTION":
    from .production import *
