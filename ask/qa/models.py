from django.db import models
from django.db.models import Q


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
    author = models.CharField(max_length=16)

    def __str__(self):
        return self.title



class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.CharField(max_length=64)

    def __str__(self):
        return self.author





