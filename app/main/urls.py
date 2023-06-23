from django.urls import path
from . import views
from .views import *
# from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.default, name='default'),
    path('api/<int:id>', FilmApiView.as_view(), name='default'),
    path('api/all', FilmApiAll.as_view(), name='FilmAll'),
    path('api/add', FilmAddView.as_view(), name='addFilm'),
    path('class/home', FilmListView.as_view(), name='default'),
    path('class/detail/<int:pk>', FilmDetailView.as_view(), name='default'),
    path('api/login/view', LoginView.as_view(), name='loginView'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('class/form', MyFormView.as_view(), name='form'),
    path('home/', views.home, name='home'),
    path("about/", MorningGreetingView.as_view()),
    path("test/", Test.as_view()),


    # path('api-token-auth/', views.obtain_auth_token),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("get-user-info/", GetUserInformation.as_view(), name="GetUserInfo"),
    path("get-all-user/", GetAllUser.as_view(), name="GetAllUser"),
    path("search-user/", SearchUser.as_view(), name="SearchUser"),



    path('getone/', GetOneData.as_view(), name="GetOneData"),
    path('getall/', GetAllData.as_view(), name="GetAllData"),


]