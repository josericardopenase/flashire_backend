from collections import UserString
from django.contrib import admin
from .models import Something, User

# Register your models here.
admin.site.register(User)
admin.site.register(Something)
