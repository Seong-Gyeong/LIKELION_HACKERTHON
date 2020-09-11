"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blog.views

from bookmark.views import BookmarkLV,BookmarkDV
#뷰 종류: LV:ListView(예: 게시판 글 목록 전체)/DV:DetailView(예 : 게시판의 특정 글 상세 내용)
app_name="Bookmark"
urlpatterns = [
    path('admin/', admin.site.urls),
    #class-based views
    path('',BookmarkLV.as_view(),name='index'),
    path('<int:pk>',BookmarkDV.as_view(),name='detail'),
    #BookmarkLV.as_view()로 URL에 맞는 View를 불러온다. 
    # name은 URL 패턴의 이름
   

    # #Blog
    # path('',blog.views.home,name='home'),
    # path('blog/<int:blog_id>',blog.views.detail,name='detail'),
    # #여기서는 객체의 int type의 blog_id 변수가 함께 넘어오게 됨.
    # # 오잉? 우리는 Blog 객체의 blog_id를 지정해준 적이 없는데?
    # #객체를 찾아오는 pk로, 데이터를 생성할 때 장고가 알아서 만들어 줌! 
    # path('blog/new/',blog.views.new,name='new'),
    # path('blog/create/',blog.views.create,name='create'),
    # path('blog/delete/<int:blog_id>',blog.views.delete,name='delete'),
    # path('blog/edit/<int:blog_id>',blog.views.edit,name='edit'),
    # path('blog/update/<int:blog_id>',blog.views.update,name='update')
]