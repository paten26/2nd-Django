from django.contrib import admin
from .models import *


# Register your models here.
class PhotosAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


# Register Admin
admin.site.register(Photos, PhotosAdmin)
admin.site.register(Comment, CommentAdmin)
