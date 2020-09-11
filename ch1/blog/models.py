from django.db import models
from django.utils import timezone

# Create your models here.
class Hashtag(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
        
class Blog(models.Model):
    title=models.CharField('title',max_length=200)
    #'타이틀'이라는 변수에서는 모델 안에 있는 문자로 되어있는 데이터를 처리
    #최대 길이는 200
    pub_date=models.DateTimeField('DATE PUBLISHED')
    body=models.TextField()
    hashtag=models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title
        #이거 안해주면 글을 작성했을 때 제목이 Blog Object(1)로 저장된다.
        #그러면 나중에 글이 많아졌을 때 뭐가 뭔지 모르니까 제목이 뜨도록 해주는 거다!

    def summary(self):
        return self.body[:100]
        #Blog 클래스 안에 본문 중에서 100글자만! 리턴해주는 함수 정의

class Comment(models.Model):
    post=models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    author_name=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.comment_text


