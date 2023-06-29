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

    path('getone/', GetOneData.as_view(), name="GetOneData"),
    path('getall/', GetAllData.as_view(), name="GetAllData"),

    # test upload img with SSR
    path('image_upload', hotel_image_view, name='image_upload'),
    path('success', success, name='success'),


    # =====================================================================================
    # =====================================================================================
    # =====================================================================================

    # REGISTER
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # USER
    path("get-user-info/", GetUserInformation.as_view(), name="GetUserInfo"),
    path("get-all-user/", GetAllUser.as_view(), name="GetAllUser"),
    path("search-user/", SearchUser.as_view(), name="SearchUser"),
    path("delete-user/<int:pk>", DeleteUser.as_view(), name="DeleteUser"),
    path("update-user/<int:pk>", UpdateUser.as_view(), name="UpdateUser"),
    path("update-user-info/", UpdateUserInfo.as_view(), name="UpdateUserInfo"),
    path("update-user-avatar/", UpdateUserAvatar.as_view(), name="UpdateUserAvatar"),
    # Movie
    path("get-all-movie/", GetAllMovie.as_view(), name="GetAllMovie"),
    path("get-movie/<int:pk>", GetOneMovie.as_view(), name="GetMovie"),
    path("search-movie/", SearchMovie.as_view(), name="SearchMovie"),
    path("delete-movie/<int:pk>", DeleteMovie.as_view(), name="DeleteMovie"),
    path("update-movie/<int:pk>", UpdateMovie.as_view(), name="UpdateMovie"),
    path("add-movie/", AddMovie.as_view(), name="AddMovie"),
    
    


]