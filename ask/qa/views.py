from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Question, Answer
from django.core.paginator import Paginator
from .forms import AskNewQuestionForm, AnswerOnQuestionForm, UserRegistrationForm


def main_page(request):
    popular_questions = Question.objects.popular()[:5]
    newest_questions = Question.objects.new()[:5]
    return render(request,
                  'main.html',
                  context={
                      'newest_questions': newest_questions, 'popular_questions': popular_questions},
                  )


@login_required
def comment(request, pk, question, form):
    if form.is_valid():
        form._user = request.user
        answer = form.save(pk)
        answer.save()
        return HttpResponseRedirect(question.get_url())


def question_num(request, **kwargs):
    pk = kwargs['pk']
    question = Question.objects.get(id=pk)
    answers = Answer.objects.filter(question=pk).order_by('-added_at')

    if request.method == 'POST':
        form = AnswerOnQuestionForm(request.POST)
        comment(request, pk, question, form)
    else:
        form = AnswerOnQuestionForm()

    return render(request, 'question.html',  {'question': question, 'answers': answers, 'form': form}, )


def popular(request):
    popular_questions = Question.objects.popular()
    paginator = Paginator(popular_questions, 5)
    page = request.GET.get('page')
    questions = paginator.get_page(page)
    return render(request,
                  'popular.html',
                  context={'questions': questions}, )


def new(request):
    newest_questions = Question.objects.new()
    paginator = Paginator(newest_questions, 5)
    page = request.GET.get('page')
    questions = paginator.get_page(page)
    return render(request, 'new.html', {'questions': questions},)


@login_required
def ask_q(request):
    if request.method == 'POST':
        form = AskNewQuestionForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AskNewQuestionForm()
    return render(request, 'ask_question.html', {'form': form},)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/accounts/login/?next=/qa/')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
