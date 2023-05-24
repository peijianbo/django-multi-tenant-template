import os

from django.core.exceptions import ImproperlyConfigured


ITOM_PROJECT_ENV = os.getenv("ITOM_PROJECT_ENV")

if not ITOM_PROJECT_ENV:
    from .dev import *
else:
    if ITOM_PROJECT_ENV == "PROD":
        from .prod import *
    elif ITOM_PROJECT_ENV == "DEV":
        from .dev import *
    else:
        raise ImproperlyConfigured("Please set the 'ITOM_PROJECT_ENV' environment variable correctly")
