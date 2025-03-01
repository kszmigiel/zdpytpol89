from django.contrib import admin

from images.models import Image, Collection, Comment, ImageLike

# Register your models here.

admin.site.register(Image)
admin.site.register(Collection)
admin.site.register(Comment)
admin.site.register(ImageLike)