import django

if django.VERSION[:2] < (1, 6):     # unittest-style discovery isn't available
    from .test_integration import *                                     # noqa
