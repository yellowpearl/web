from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Question, QuestionManager, Answer
from django.core.paginator import Paginator
from .forms import AskNewQuestionForm, AnswerOnQuestionForm


def main_page(request):
    popular_questions = Question.objects.popular()[:5]
    newest_questions = Question.objects.new()[:5]
    return render(request,
                  'main.html',
                  context={
                      'newest_questions': newest_questions, 'popular_questions': popular_questions},
                  )


def question_num(request, **kwargs):
    pk = kwargs['pk']
    question = Question.objects.get(id=pk)
    answers = Answer.objects.filter(question=pk).order_by('-added_at')

    if request.method == 'POST':
        form = AnswerOnQuestionForm(request.POST)
        if form.is_valid():
            answer = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AnswerOnQuestionForm()

    return render(request,
                  'question.html',
                  context={'question': question, 'answers': answers, 'form': form}, )


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
    return render(request,
                  'new.html',
                  context={'questions': questions},)


def ask_q(request):
    if request.method == 'POST':
        form = AskNewQuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AskNewQuestionForm()
    return render(request,
                  'ask_question.html',
                  context={
                      'form': form
                  },)


def login(request, *args, **kwargs):
    return HttpResponse('OK')


def signup(request, *args, **kwargs):
    return HttpResponse('OK')



