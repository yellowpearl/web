from django import forms
from .models import Question, Answer


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

    def __init__(self, q_fk):
        super().__init__()
        self.q_fk = q_fk

    def clean_text(self):
        text = self.cleaned_data['text']
        if text == '':
            raise forms.ValidationError('Empty field', code=0)
        return text

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.question = self.q_fk
        answer.save()
        return answer
