from django.contrib import admin
from .models import Blog,Hashtag,Comment
# Register your models here.
admin.site.register(Blog)
admin.site.register(Hashtag)
admin.site.register(Comment)