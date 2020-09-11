from django.db import models

# Create your models here.
class Bookmark(models.Model):
    title=models.CharField('TITLE',max_length=100,blank='True')
    #CharField:제한된 문자열 필드 타입. 최대 길이를 max_length 옵션에 지정
    #blank=true: 필드가 폼(입력 양식)에서 빈 채로 저장되는 것을 허용
    url=models.URLField('URL',unique=True)
    #원래는 모든 필드에 대해서 unique라는 옵션이 false로 되어있습니다. 이때는 이 url이라는 필드 안에, 중복된 값이 들어올 수 있습니다.
    #예를들어, 제가 naver에 www.naver.com을 넣고, daum에도 www.naver.com을 url에 저장할 수 있는 것이죠. 
    #unique=true 를 통해 이 옵션을 true로 바꾸게되면, url 필드 안에 중복된 값이 저장되면 장고가 에러를 발생시키게 됩니다.

    def __str__(self):
        #인스턴스 자체를 출력 할 때의 형식을 지정해주는 함수
        return self.title