from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.default, name='default'),
    path('api/<int:id>', FilmApiView.as_view(), name='default'),
    path('class/home', FilmListView.as_view(), name='default'),
    path('class/detail/<int:pk>', FilmDetailView.as_view(), name='default'),
    path('api/login/view', LoginView.as_view(), name='loginView'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('class/form', MyFormView.as_view(), name='form'),
    path('home/', views.home, name='home'),
    path("about/", MorningGreetingView.as_view()),
    path("test/", Test.as_view()),
]