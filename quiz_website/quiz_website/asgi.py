"""
ASGI config for quiz_website project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_website.settings')

application = get_asgi_application()

# {
#   "user": {
#     "name": "ohn joe",
#     "student_number": "12389",
#     "email": "hn.oe@akgec.ac.in"
#   },
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI0NTE3OTExLCJpYXQiOjE3MjQ1MTc2MTEsImp0aSI6IjFmYTE1MmUyNDFhYzRiMTdiYzgyMWNjNmMyZGIyZjBhIiwidXNlcl9pZCI6NX0.c7pnxuQb5GDY2Lkq89vli3quZonH3Lzu57b0lONZw8Q",
#   "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDYwNDAxMSwiaWF0IjoxNzI0NTE3NjExLCJqdGkiOiI3NWJmZDkwMzQ0MGI0ZDJlYWE5ZWRmNTFlMGI5NTIyOCIsInVzZXJfaWQiOjV9.OITUj43fiJWl4uJ98HMEoqrLGKiGm7f_faeEtsf5TPk"
# }
