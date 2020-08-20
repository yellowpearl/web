from django.db import models
from django.contrib.auth.models import User
import time


class QuestionManager(models.Manager):
    def new(self):
        """
        return questions ordered by 'added_at' from db
        """
        return self.order_by('-added_at')

    def popular(self):
        """
        return questions ordered by 'rating' from db
        """
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=32)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_url(self):
        prim_key = str(self.pk)
        return 'http://0.0.0.0:8000/qa/question/'+str(prim_key)

    def get_time(self):
        return self.added_at.strftime('%d.%m.%Y %H:%M')

    def short_text(self):
        if len(self.text)>140:
            return self.text[:140]+'...'
        else:
            return self.text


class Answer(models.Model):
    objects = QuestionManager()
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.author

    def get_time(self):
        return self.added_at.strftime('%d.%m.%Y %H:%M')
