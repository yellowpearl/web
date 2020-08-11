from django.contrib import admin

from .models import UserName, Question, Answer

admin.site.register(UserName)
admin.site.register(Question)
admin.site.register(Answer)