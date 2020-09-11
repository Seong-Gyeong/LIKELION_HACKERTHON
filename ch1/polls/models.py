from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

        #def __str__(self)-인스턴스 자체를 출력할 때 형식을 지정해주는 함수
        #'사과'는 클래스, '내가 엊저녁에 먹은 사과 다섯 개 중에 두 번째 것'이라고 콕 찍어서 말해주면 실체(instance)

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text