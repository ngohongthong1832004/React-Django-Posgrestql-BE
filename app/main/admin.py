from django.contrib import admin

# Register your models here.

from .models import  Film, UserSub
admin.site.register(Film)
admin.site.register(UserSub)
