from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from bookmark.models import Bookmark

class BookmarkLV(ListView):
    model=Bookmark
    #model에서 만들어 둔 Bookmark 테이블을 가져온다.

class BookmarkDV(DetailView):
    model=Bookmark