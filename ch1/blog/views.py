from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .forms import CommentForm
# Create your views here.
def home(request):
    blogs=Blog.objects
    #model에 있는 글을 html파일에 어떻게 띄울 것인가?!
    #Blog 클래스로 형성된 객체들을 blogs 변수에 담아주고, 이를
    
    return render(request,'home.html',{'blogs':blogs})
    #view에서 home을 처리할 때 같이 받아와서 사전형 인자로 전달한다. 

# 렌더링 : 템플릿 코드를 템플릿 파일로 해석하는 과정
#render 함수 (3개 인자 가능) 내에 request 객체, home.html 객체를 받는다

#urls.py에 'home'이라는 이름의 url이 있는데 이거에 맞는 요청이 들어오면
#view가 home.html을 리턴해준다. 

def detail(request,blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)
                                #(어떤 클래스, 검색조건(몇번데이터, pk))
    hashtags=blog_detail.hashtag.all()
    return render(request,'detail.html',{'blog':blog_detail, 'hashtags':hashtags})
    
def new(request):
    return render(request,'new.html')

def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    #new.html에서 'title'이라는 form에 입력한 내용을 여기로 가져와서
    #blog라는 객체의 title 변수에 담아주기
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    #blog라는 객체에 넣어줬던 내용들을 데이터베이스에 저장해라
    return redirect('/blog/'+str(blog.id))

def delete(request,blog_id):
    blog=Blog.objects.get(pk=blog_id)
    blog.delete()
    return redirect('home')

def edit(request,blog_id):
    blog_edit=Blog.objects.get(pk=blog_id)
    return render(request,'edit.html',{'blog':blog_edit})

@csrf_exempt
def update(request,blog_id):
    blog=Blog.objects.get(pk=blog_id)
    blog.title=request.POST['title']
    blog.body=request.POST['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('home')

def add_comment_to_post(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=blog
            comment.save()
            return redirect('blog:detail',blog_id)

    else:
            form=CommentForm()

    return render(request,'add_comment_to_post.html',{'form':form})
