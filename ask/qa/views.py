from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, QuestionManager, Answer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def main_page(request, *args, **kwargs):
    popular_questions = Question.objects.popular()[:5]
    newest_questions = Question.objects.new()[:5]
    return render(request,
                  'main.html',
                  context={
                      'newest_questions': newest_questions, 'popular_questions': popular_questions},
                  )


def login(request, *args, **kwargs):
    return HttpResponse('OK')


def signup(request, *args, **kwargs):
    return HttpResponse('OK')


def question_num(request, *args, **kwargs):
    pk = kwargs['pk']
    question = Question.objects.get(id=pk)
    q_title = question.title
    q_author = question.author
    q_text = question.text
    return render(request,
                  'question.html',
                  context={'title': q_title,
                           'text': q_text,
                           'author': q_author
                           }, )





def ask_q(request, *args, **kwargs):
    return HttpResponse('OK')


def popular(request, *args, **kwargs):
    popular_questions = Question.objects.popular()
    paginator = Paginator(popular_questions, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'popular.html',
                  context={'popular_questions': popular_questions, 'page': page, 'posts': posts}, )


def new(request, *args, **kwargs):
    newest_questions = Question.objects.new()[:]
    paginator = Paginator(newest_questions, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'new.html',
                  context={'newest_questions': newest_questions, 'page': page, 'posts': posts},)


def test(request, *args, **kwargs):
    return HttpResponse('OK')