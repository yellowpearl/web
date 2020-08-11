from django.db import models


class UserName(models.Model):
    name = models.CharField(max_length=64)


class Question(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(default=0)
    author = models.OneToOneField(UserName, null=True, on_delete=models.SET_NULL)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.OneToOneField(UserName, null=True, on_delete=models.SET_NULL)
