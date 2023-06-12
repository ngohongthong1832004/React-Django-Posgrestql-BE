from django.contrib import admin

# Register your models here.

from .models import  Film, UserSub,Movies
admin.site.register(Movies)
admin.site.register(Film)
admin.site.register(UserSub)
