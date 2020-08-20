from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User


class AskNewQuestionForm(forms.Form):
    title = forms.CharField(max_length=32)
    text = forms.CharField(max_length=300)

    def clean_title(self):
        title = self.cleaned_data['title']
        if title == '':
            raise forms.ValidationError('Empty field', code=0)
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if text == '':
            raise forms.ValidationError('Empty field', code=0)
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.author = self._user
        question.save()
        return question


class AnswerOnQuestionForm(forms.Form):
    text = forms.CharField(max_length=300)

    def clean_text(self):
        text = self.cleaned_data['text']
        if text == '':
            raise forms.ValidationError('Empty field', code=0)
        return text

    def save(self, fk):
        answer = Answer(**self.cleaned_data)
        answer.author = self._user
        answer.question_id = fk
        answer.save()
        return answer


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=16)
    email = forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def save(self):
        user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password'])
        return user
