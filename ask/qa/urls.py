from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main_page),
    path('login', views.login),
    path('signup', views.signup),
    path('question/<int:pk>', views.question_num),
    path('ask', views.ask_q),
    path('popular', views.popular),
    path('new', views.new),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)