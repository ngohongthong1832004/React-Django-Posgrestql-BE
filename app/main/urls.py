from django.urls import path
from . import views
from main.views import GreetingView

urlpatterns = [
    path('', views.default, name='default'),
    path('home/', views.home, name='home'),
    path("about/", GreetingView.as_view()),
]