from decouple import config

if config("DJANGO_ENV") == "DEBUG":
    from .debug import *
if config("DJANGO_ENV") == "DEV":
    from .dev import *
if config("DJANGO_ENV") == "PROD":
    from .prod import *
