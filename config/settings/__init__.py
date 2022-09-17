from decouple import config

environment = config("DJANGO_ENV", "DEBUG")

if environment == "DEBUG":
    from .debug import *
if environment == "DEV":
    from .dev import *
if environment == "PROD":
    from .prod import *
