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
    # Movie for staff
    path("delete-movie/<int:pk>", DeleteMovie.as_view(), name="DeleteMovie"),
    path("update-movie/<int:pk>", UpdateMovie.as_view(), name="UpdateMovie"),
    path("add-movie/", AddMovie.as_view(), name="AddMovie"),
    # Movie for user
    path("get-all-movie/", GetAllMovie.as_view(), name="GetAllMovie"),
    path("get-movie/<int:pk>", GetOneMovie.as_view(), name="GetMovie"),
    path("search-movie/", SearchMovie.as_view(), name="SearchMovie"),
    path("search-movie-with-genre/", SearchMovieWithGenre.as_view(), name="SearchMovieWithGenre"),
    path("search-movie-with-cast/", SearchMovieWithCast.as_view(), name="SearchMovieWithActor"),
    path("search-movie-with-country/", SearchMovieWithCountry.as_view(), name="SearchMovieWithCountry"),
    path("search-movie-with-description/", SearchMovieWithDescription.as_view(), name="SearchMovieWithDescription"),   
    path("search-movie-with-chat/", SearchMovieWithChat.as_view(), name="SearchMovieWithChat"), 
    path("get-random-movie/", GetRandomMovie.as_view(), name="GetRandomMovie"),
   
    # path("get-wishlist-like/", GetWishlistLike.as_view(), name="GetMovieWishlistLike"),
    # path("get-wishlist-like-id/", GetWishlistLikeId.as_view(), name="GetMovieWishlistLikeId"),
    # path("get-wishlist-follow/", GetWishlistFollow.as_view(), name="GetMovieWishlistFollow"),
    # path("get-wishlist-follow-id/", GetWishlistFollowId.as_view(), name="GetMovieWishlistFollowId"),
    # path("like-movie/", LikeMovie.as_view(), name="LikeMovie"),
    # path("follow-movie/", FollowMovie.as_view(), name="FollowMovie"),

    path("toggle-wishlist-like/", ToggleWishlistLike.as_view(), name="ToggleWishlistLike"),
    path("toggle-wishlist-follow/", ToggleWishlistFollow.as_view(), name="ToggleWishlistFollow"),
    path("get-all-id-movie-wishlist-like/", GetAllIdMovieWishlistLike.as_view(), name="GetAllIdMovieWishlistLike"),
    path("get-all-id-movie-wishlist-follow/", GetAllIdMovieWishlistFollow.as_view(), name="GetAllIdMovieWishlistFollow"),
    path("get-movie-wishlist-like/", GetMovieWishlistLike.as_view(), name="GetMovieWishlistLike"),
    path("get-movie-wishlist-follow/", GetMovieWishlistFollow.as_view(), name="GetMovieWishlistFollow"),

    # Chat
    path("add-chat-item/", AddChatItem.as_view(), name="AddChatItem"),
    path("get-chat-item/", GetChatItem.as_view(), name="GetChatItem"),
    path("add-chat-reply/", AddChatReply.as_view(), name="AddChatReply"),

    path("like-chat-item/", LikeChatItem.as_view(), name="LikeChatItem"),
    path("like-chat-reply/", LikeChatReply.as_view(), name="LikeChatReply"),
    path("delete-chat-item/<int:pk>", DeleteChatItem.as_view(), name="DeleteChatItem"),
    path("delete-chat-reply/<int:pk>", DeleteChatReply.as_view(), name="DeleteChatReply"),
    path("dislike-chat-item/", DislikeChatItem.as_view(), name="DislikeChatItem"),
    path("dislike-chat-reply/", DisLikeChatReply.as_view(), name="DislikeChatReply"),

]