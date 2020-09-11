from django.contrib import admin
from bookmark.models import Bookmark
# Register your models here.
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display=('id','title','url')
    #Admin 목록에 보여질 필드 목록