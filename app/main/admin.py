from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(InfoUser)
admin.site.register(Movie)
admin.site.register(ChatBox)
admin.site.register(ChatItem)
admin.site.register(ChatReply)
admin.site.register(WishlistLike)
admin.site.register(WishlistFollow)
# admin.site.register(Hotel)
