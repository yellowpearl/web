from django import forms
from .models import Question, Answer, User


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
        answer.question_id = fk
        answer.save()
        return answer


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=16)
    email = forms.EmailField(max_length=32)
    password = forms.CharField(widget=forms.PasswordInput())

    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=16)
    password = forms.PasswordInput()
