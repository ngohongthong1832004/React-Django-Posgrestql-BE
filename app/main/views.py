from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.generic.edit import FormView
from django.db.models import Q, F
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.core.management import call_command

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser, FormParser

import socket



from .models import *

from datetime import date

from main.serializers import *

from .forms import *


# CUSTOM pagination
class CustomPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 100

def CustomDataPagination(data, request):
    pagination_class = CustomPagination()
    paginated_items = pagination_class.paginate_queryset(data, request)
    rs = {
        "data" : paginated_items,
        "pagination" : {
            "total" : len(data),
            "max_page" : pagination_class.page.paginator.num_pages,
            "current_page" : pagination_class.page.number,
            "next_page" : pagination_class.get_next_link(),
            "previous_page" : pagination_class.get_previous_link(),
        }
    }
    return rs

class CustomPaginationChat(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

def CustomDataPaginationChat(data, request):
    pagination_class = CustomPaginationChat()
    paginated_items = pagination_class.paginate_queryset(data, request)
    rs = {
        "data" : paginated_items,
        "pagination" : {
            "total" : len(data),
            "max_page" : pagination_class.page.paginator.num_pages,
            "current_page" : pagination_class.page.number,
            "next_page" : pagination_class.get_next_link(),
            "previous_page" : pagination_class.get_previous_link(),
        }
    }
    return rs



class LoginView(FormView) :
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        print("==========================================================================")
        print(username , password)
        user = authenticate(username=username, password=password)

        if user is not None:
            # User credentials are valid
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # User credentials are invalid
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().form_valid(form)
class LoginAPIView(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
class FilmApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, *args, **kwargs):
        films = Film.objects.all()
        film = films.filter(id=kwargs['id'])
        serializer = FilmSerializer(film, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class FilmApiAll(APIView):

    pagination_class = CustomPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        paginator = self.pagination_class()
        films = Movie.objects.all()
        paginated_items = paginator.paginate_queryset(films, request)
        serializer = FilmSerializer(paginated_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class FilmAddView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def post(self, request):
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def home(request):
    return HttpResponse("Hello world! my friends")
def default(request):
    current_date = date.today()
    test = {
        "name": "Pine",
        "age": current_date.year - 2004,
        "HELLO" : "Welcome to my world",
        "♠○☺☻♥" : "I LOVE YOU",
    }

    return JsonResponse(test, safe=False)
class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)
class MorningGreetingView(GreetingView):
    greeting = "Morning to ya"
class Test(DetailView):
    model = Film
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_list"] = Film.objects.all()
        return context
class FilmListView(LoginRequiredMixin, ListView):
    model = Film
    template_name = 'home.html'
    context_object_name = 'film_list'
    queryset = Film.objects.all()
    def get_queryset(self):
        return Film.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['film_list'] = Film.objects.all()
        return context
class FilmDetailView(DetailView):
    model = Film

    template_name = 'detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['film'] = Film.objects.get(id=self.kwargs['pk'])
        context['testContext'] = Film.objects.get(id=self.kwargs['pk'])
        context["year"] = Film.objects.get(id=self.kwargs['pk']).year
        return context
class MyFormView(FormView):
    template_name = 'form.html'
    form_class = MyForm
    success_url = 'home'  # URL to redirect to after successful form submission
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        # print(name, email, message)
        return super().form_valid(form)
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
def hotel_image_view(request):
    
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'uploadImg.html', {'form': form})
def success(request):
    return HttpResponse('successfully uploaded')
class GetOneData(APIView):
    permission_classes = [IsAuthenticated]
  
    def get(self, request, *args, **kwargs):
        # user = request.user
        return Response({'message': "user.username"})
class GetAllData(APIView):
    permission_classes = [IsAuthenticated]
    model = Movie
    serializer = MovieSerializer(model.objects.all(), many=True)
    def get(self, request, *args, **kwargs):
        paginator = CustomPagination()
        paginated_items = paginator.paginate_queryset(self.serializer.data, request)
        return Response(paginated_items, status=status.HTTP_200_OK)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# =====================================================================================================================================
# =====================================================================================================================================
# =====================================================================================================================================
# =====================================================================================================================================

# handle creae super user





# API RESTFULL



# ======================================================================================================
# ======================================================================================================
# Register


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print(user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email,
            'isStaff' : user.is_staff,
            'firstName' : user.first_name,
            'lastName' : user.last_name,
            "isSuperuser" : user.is_superuser,
        })
    

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response({'message': 'Logout successful'})


# ======================================================================================================
# ======================================================================================================
# End Register




# ======================================================================================================
# ======================================================================================================
# Users
class GetUserInformation(APIView):
    permission_classes = [IsAuthenticated]
    model = InfoUser
    # serializers = InfoUserSerializer(model.objects.all(), many=True)
    def get(self, request):
        user = request.user
        info_user = InfoUser.objects.get(user=user)
        serializer = InfoUserSerializer(info_user)
        return Response({
            'email': user.email,
            "isSuperuser" : user.is_superuser,
            'isStaff' : user.is_staff,
            "infoUser": serializer.data,
            "fullname": user.first_name + " " + user.last_name,
        })

class GetAllUser(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(CustomDataPagination(serializer.data, request), status=status.HTTP_200_OK)

        
class SearchUser(APIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()

    def post(self, request):
        search_value = request.data.get('searchValue')
        if " " in search_value:
            search_value = search_value.split(" ")
            users = self.queryset.filter(
                Q(first_name__startswith=search_value[0]) &
                Q(last_name__icontains=search_value[1])
        )
        else:
            users = self.queryset.filter(
                Q(first_name__startswith=search_value) |
                Q(last_name__icontains=search_value)
            )
        serializer = UserSerializer(users, many=True)
        return Response(CustomDataPagination(serializer.data, request), status=status.HTTP_200_OK)
    
class DeleteUser(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        user.delete()
        return Response({'message': 'Delete successful'})

class UpdateUser(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        user.is_staff = True
        user.save()
        return Response({'message': 'Set staff successful'})
    
class UpdateUserInfo(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user  = request.user
        user.first_name = request.data.get('first_name')
        user.last_name = request.data.get('last_name')
        user.save()
        return Response({
            "first_name": user.first_name,
            "last_name": user.last_name,
        })
    

class UpdateUserAvatar(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]



    def post(self, request, *args, **kwargs):
        fqdn = socket.getfqdn()
        ip_address = socket.gethostbyname(fqdn)
        domain = request.META.get('HTTP_HOST')


        user = InfoUser.objects.get(user=request.user)
        avatar_file = request.FILES.get('avatar')

        print("ip_address: ", ip_address)
        print("domain: ", domain)

        if avatar_file:
            # Save the file or perform other processing here
            user.avatar.save(avatar_file.name, avatar_file, save=True)
            
            return Response({
                "avatarURL": domain + user.avatar.url,
            })
        else:
            return Response({'error': 'No avatar file provided.'}, status=400)


# ======================================================================================================
# ======================================================================================================
# End Users
    

# ======================================================================================================
# ======================================================================================================
# Movies

class ToggleWishlistLike(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        idMovie = request.data.get('movieId')
        movie = Movie.objects.get(id=idMovie)
        wishlist = WishlistLike.objects.filter(user=user, movie=movie)
        if wishlist:
            wishlist.delete()
            movie.like -= 1
            movie.save()
            InfoUser.objects.filter(user=user).update(countLike=F('countLike') - 1)
            return Response({'message': 'Delete wishlist like successful'})
        else:
            WishlistLike.objects.create(user=user, movie=movie)
            movie.like += 1
            movie.save()
            InfoUser.objects.filter(user=user).update(countLike=F('countLike') + 1)
            print(movie.like)
            return Response({'message': 'Add wishlist like successful'})
class ToggleWishlistFollow(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        idMovie = request.data.get('movieId')
        movie = Movie.objects.get(id=idMovie)
        wishlist = WishlistFollow.objects.filter(user=user, movie=movie)
        if wishlist:
            wishlist.delete()
            InfoUser.objects.filter(user=user).update(countWishlist=F('countWishlist') - 1)
            return Response({'message': 'Delete wishlist follow successful'})
        else:
            WishlistFollow.objects.create(user=user, movie=movie)
            InfoUser.objects.filter(user=user).update(countWishlist=F('countWishlist') + 1)
            return Response({'message': 'Add wishlist follow successful'})
        

class GetMovieWishlistLike(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        wishlist = WishlistLike.objects.filter(user=user)
        movies = []
        for item in wishlist:
            movie = item.movie
            movies.append(movie)
        
        serializer = MovieSerializer(movies, many=True)
        return Response(CustomDataPagination(serializer.data, request), status=status.HTTP_200_OK)
class GetMovieWishlistFollow(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        wishlist = WishlistFollow.objects.filter(user=user)
        movies = []
        for item in wishlist:
            movie = item.movie
            movies.append(movie)
        
        serializer = MovieSerializer(movies, many=True)
        return Response(CustomDataPagination(serializer.data, request), status=status.HTTP_200_OK)

class GetAllIdMovieWishlistLike(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        wishlist = WishlistLike.objects.filter(user=user)
        movies = []
        for item in wishlist:
            movie = item.movie
            movies.append(movie)
        
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetAllIdMovieWishlistFollow(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        wishlist = WishlistFollow.objects.filter(user=user)
        movies = []
        for item in wishlist:
            movie = item.movie
            movies.append(movie)
        
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class GetWishlistLike(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request):
#         user = request.user
#         idMovie = request.data.get('movieId')
#         movie = Movie.objects.get(id=idMovie)
#         wishlists = WishlistLike.objects.filter(user=user, movie=movie)
#         movies = []
#         for wishlist in wishlists:
#             movie = wishlist.movie
#             movies.append(movie)
        
#         serializer = MovieSerializer(movies, many=True)
#         return Response(CustomDataPagination(serializer.data, request), status=status.HTTP_200_OK)

# class GetWishlistLikeId(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request):
#         user = request.user
#         idMovie = request.data.get('movieId')
#         movie = Movie.objects.get(id=idMovie)
#         wishlists = WishlistLike.objects.filter(user=user, movie=movie)
#         movies = []
#         for wishlist in wishlists:
#             movie = wishlist.movie
#             movies.append(movie)
        
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class GetWishlistFollow(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request):
#         user = request.user
#         idMovie = request.data.get('movieId')
#         movie = Movie.objects.get(id=idMovie)
#         wishlists = WishlistFollow.objects.filter(user=user, movie = movie)
#         movies = []
#         for wishlist in wishlists:
#             movie = wishlist.movie
#             movies.append(movie)
        
#         serializer = MovieSerializer(movies, many=True)
#         return Response(CustomDataPagination(serializer.data, request), status=status.HTTP_200_OK)

# class GetWishlistFollowId(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request):
#         user = request.user
#         idMovie = request.data.get('movieId')
#         movie = Movie.objects.get(id=idMovie)
#         wishlists = WishlistFollow.objects.filter(user=user, movie = movie)
#         movies = []
#         for wishlist in wishlists:
#             movie = wishlist.movie
#             movies.append(movie)
        
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class LikeMovie(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request):
#         user = request.user
#         idMovie = request.data.get('movieId')
#         wishlist, created = WishlistLike.objects.get_or_create(user=user, idMovie=idMovie)
        
#         if created:
#             return Response({'message': 'Like movie successful'})
#         else:
#             if wishlist.isLikeOrFollow:
#                 wishlist.delete()
#                 return Response({'message': 'Unlike movie successful'})
#             else:
#                 wishlist.isLikeOrFollow = True
#                 wishlist.save()
#                 return Response({'message': 'Like movie successful'})

# class FollowMovie(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request):
#         user = request.user
#         idMovie = request.data.get('movieId')
#         wishlist, created = WishlistFollow.objects.get_or_create(user=user, idMovie=idMovie)

#         if created:
#             return Response({'message': 'Follow movie successful'})
#         else:
#             if not wishlist.isLikeOrFollow:
#                 wishlist.delete()
#                 return Response({'message': 'Unfollow movie successful'})
#             else:
#                 wishlist.isLikeOrFollow = False
#                 wishlist.save()
#                 return Response({'message': 'Follow movie successful'})


class GetAllMovie(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        serializer = MovieSerializer(Movie.objects.all(), many=True)
        return Response(CustomDataPagination(serializer.data, request), status=status.HTTP_200_OK)

class GetOneMovie(APIView):
    permission_classes = [AllowAny]
    model = Movie
    serializer = MovieSerializer(model.objects.all(), many=True)
    def get(self, request, *args, **kwargs):
        movie = Movie.objects.get(id=kwargs['pk'])
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetRandomMovie(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        movies = Movie.objects.all().order_by('?')[:5]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SearchMovie(APIView):
    permission_classes = [AllowAny]
    queryset = Movie.objects.all()

    def post(self, request):
        search_value = request.data.get('searchValue')
        movies = self.queryset.filter(
            Q(name__startswith=search_value) |
            Q(subName__startswith=search_value)
        )
        serializer = MovieSerializer(movies, many=True)
        return Response(CustomDataPagination(serializer.data, request), status=status.HTTP_200_OK)

class SearchMovieWithGenre(APIView):
    permission_classes = [AllowAny]
    queryset = Movie.objects.all()

    def post(self, request) : 
        genre = request.data.get('searchValue')
        movies = self.queryset.filter(
            Q(genres__icontains=genre)
        )
        serializer = MovieSerializer(movies, many=True)
        return Response(CustomDataPagination(serializer.data, request), status=status.HTTP_200_OK)


class SearchMovieWithCast(APIView):
    permission_classes = [AllowAny]
    queryset = Movie.objects.all()

    def post(self, request) : 
        cast = request.data.get('searchValue')
        movies = self.queryset.filter(
            Q(casts__icontains=cast)
        )
        serializer = MovieSerializer(movies, many=True)
        return Response(CustomDataPagination(serializer.data, request), status=status.HTTP_200_OK)

class SearchMovieWithChat(APIView):
    permission_classes = [AllowAny]
    queryset = Movie.objects.all()

    def post(self, request) : 
        chat = request.data.get('searchValue')
        movies = self.queryset.filter(
            Q(chats__icontains=chat)
        )
        serializer = MovieSerializer(movies, many=True)
        return Response(CustomDataPagination(serializer.data, request), status=status.HTTP_200_OK)

class SearchMovieWithCountry(APIView):
    permission_classes = [AllowAny]
    queryset = Movie.objects.all()

    def post(self, request) : 
        country = request.data.get('searchValue')
        movies = self.queryset.filter(
            Q(countries__icontains=country)
        )
        serializer = MovieSerializer(movies, many=True)
        return Response(CustomDataPagination(serializer.data, request), status=status.HTTP_200_OK)

class SearchMovieWithDescription(APIView):
    permission_classes = [AllowAny]
    queryset = Movie.objects.all()
    def post(self,request) :
        description = request.data.get('searchValue')
        movies = self.queryset.filter(
            Q(desc__icontains=description)
        )
        serializer = MovieSerializer(movies, many=True)
        return Response(CustomDataPagination(serializer.data, request), status=status.HTTP_200_OK)


class AddMovie(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        if user.is_staff == False:
            return Response({'message': 'You do not have permission to do this action'})
        
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Add movie successful'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UpdateMovie(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user = request.user

        if user.is_staff == False:
            return Response({'message': 'You do not have permission to do this action'})
        movie = Movie.objects.get(id=kwargs['pk'])
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Update movie successful'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteMovie(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, *args, **kwargs):
        movie = Movie.objects.get(id=kwargs['pk'])
        movie.delete()
        return Response({'message': 'Delete movie successful'})

# ======================================================================================================
# ======================================================================================================
# End Movies



# ======================================================================================================
# ======================================================================================================
# Chat

class AddChatItem(APIView) :
    permission_classes = [IsAuthenticated]
    def post(self, request) :
        user = request.user
        userInfo = InfoUser.objects.get(user=user)
        userInfo.countComment += 1
        userInfo.save()
        movie = Movie.objects.get(id=request.data.get('movieId'))
        chat_box = ChatBox.objects.get(movies=movie)
        chat_item = ChatItem.objects.create(user=user, chatbox=chat_box, content=request.data.get('content'))
        chat_box.totalChatItem += 1
        chat_box.save()
        serializer = ChatItemSerializer(chat_item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class GetChatItem(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        checkDelete = request.user 
        result = []
        idMovie = request.data.get('movieId')
        movie = Movie.objects.get(id=idMovie)
        chat_box = ChatBox.objects.get(movies=movie)
        chat_items = ChatItem.objects.filter(chatbox=chat_box).order_by('-id')

        for chatItem in chat_items:
            user_info = InfoUser.objects.get(user=chatItem.user)
            chat_replies = ChatReply.objects.filter(chatitem=chatItem)
            # chat_replies_serializer = ChatReplySerializer(chat_replies, many=True)
            full_name = (
                chatItem.user.first_name + " " + chatItem.user.last_name
            ) or chatItem.user.username.split("@")[0]
            item = {
                "data": {
                    "user": {
                        "id": chatItem.user.id,
                        "username": full_name,
                        "avatar": user_info.avatar.url if user_info.avatar else None,
                        "isStaff" : chatItem.user.is_staff,
                        "isSuperuser" : chatItem.user.is_superuser,
                    },
                    "chatItem": {
                        "id": chatItem.id,
                        "content": chatItem.content,
                        "created_at": chatItem.created_at.strftime("%d/%m/%Y %H:%M"),
                        "isDelete": checkDelete == chatItem.user,
                        "like" : chatItem.like,
                    },
                    "chatReply": {
                        "data": [],
                    }
                }
            }
            for chatReply in chat_replies[::-1]:
                user_info = InfoUser.objects.get(user=chatReply.user)
                full_name = (
                    chatReply.user.first_name + " " + chatReply.user.last_name
                ) or chatReply.user.username.split("@")[0]
                chatReplyObj = {
                    "id": chatReply.id,
                    "user": {
                        "id": chatReply.user.id,
                        "username": full_name,
                        "avatar": user_info.avatar.url if user_info.avatar else None,
                        "isStaff" : chatReply.user.is_staff,
                        "isSuperuser" : chatReply.user.is_superuser,
                        "isDelete": checkDelete == chatReply.user,
                    },
                    "like" : chatReply.like,
                    "content": chatReply.content,
                    "created_at": chatReply.created_at.strftime("%d/%m/%Y %H:%M"),
                }
                item["data"]["chatReply"]["data"].append(chatReplyObj)
            result.append(item)

        return Response(CustomDataPaginationChat(result, request), status=status.HTTP_200_OK)


class AddChatReply(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request) :
        user = request.user
        userInfo = InfoUser.objects.get(user=user)
        userInfo.countComment += 1
        userInfo.save()
        chat_item = ChatItem.objects.get(id=request.data.get('chatItemId'))
        chat_reply = ChatReply.objects.create(user=user, chatitem=chat_item, content=request.data.get('content'))
        # get boc cha
        serializer = ChatReplySerializer(chat_reply)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class DeleteChatItem(APIView) : 
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs) :
        user = request.user
        userInfo = InfoUser.objects.get(user=user)
        chat_item = ChatItem.objects.get(id=kwargs['pk'])
        chatreply = ChatReply.objects.filter(chatitem=chat_item)
        userInfo.countComment = userInfo.countComment - ( 1 + len(chatreply) ) 
        userInfo.save()
        if user == chat_item.user :
            chat_item.delete()
            return Response({'message': 'Delete chat item successful'})
        else :
            return Response({'message': 'You do not have permission to do this action'})
        
class DeleteChatReply(APIView) :
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs) :
        user = request.user
        userInfo = InfoUser.objects.get(user=user)
        userInfo.countComment -= 1
        userInfo.save()
        chat_reply = ChatReply.objects.get(id=kwargs['pk'])
        if user == chat_reply.user :
            chat_reply.delete()
            return Response({'message': 'Delete chat reply successful'})
        else :
            return Response({'message': 'You do not have permission to do this action'})
    
class LikeChatItemView(APIView) :
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user = request.user
        chat_item = ChatItem.objects.get(id=kwargs['pk'])
        if LikeChatItem.objects.filter(user=user, chatitem=chat_item).exists():
            LikeChatItem.objects.filter(user=user, chatitem=chat_item).delete()
            chat_item.like -= 1
            chat_item.save()
            return Response({'message': 'You have liked this chat item'})
        if DisLikeChatItem.objects.filter(user=user, chatitem=chat_item).exists():
            DisLikeChatItem.objects.filter(user=user, chatitem=chat_item).delete()
        LikeChatItem.objects.create(user=user, chatitem=chat_item)
        chat_item.like += 1
        chat_item.save()
        return Response({'message': 'Like chat item successful'})

class LikeChatReplyView(APIView) :
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user = request.user
        chat_reply = ChatReply.objects.get(id=kwargs['pk'])
        if LikeChatReply.objects.filter(user=user, chatreply=chat_reply).exists():
            LikeChatReply.objects.filter(user=user, chatreply=chat_reply).delete()
            chat_reply.like -= 1
            chat_reply.save()
            return Response({'message': 'You have liked this chat reply'})
        if DisLikeChatReply.objects.filter(user=user, chatreply=chat_reply).exists():
            DisLikeChatReply.objects.filter(user=user, chatreply=chat_reply).delete()
        LikeChatReply.objects.create(user=user, chatreply=chat_reply)
        chat_reply.like += 1
        chat_reply.save()
        return Response({'message': 'Like chat reply successful'})
    
class DislikeChatItemView(APIView) :
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user = request.user
        chat_item = ChatItem.objects.get(id=kwargs['pk'])
        if DisLikeChatItem.objects.filter(user=user, chatitem=chat_item).exists():
            DisLikeChatItem.objects.filter(user=user, chatitem=chat_item).delete()
            return Response({'message': 'You have disliked this chat item'})
        DisLikeChatItem.objects.create(user=user, chatitem=chat_item)
        LikeChatItem.objects.filter(user=user, chatitem=chat_item).delete()
        chat_item.like -= 1
        chat_item.save()
        return Response({'message': 'Dislike chat item successful'})
class DisLikeChatReplyView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user = request.user
        chat_reply = ChatReply.objects.get(id=kwargs['pk'])
        if DisLikeChatReply.objects.filter(user=user, chatreply=chat_reply).exists():
            DisLikeChatReply.objects.filter(user=user, chatreply=chat_reply).delete()
            return Response({'message': 'You have disliked this chat reply'})
        DisLikeChatReply.objects.create(user=user, chatreply=chat_reply)
        LikeChatReply.objects.filter(user=user, chatreply=chat_reply).delete()
        chat_reply.like -= 1
        chat_reply.save()
        return Response({'message': 'Dislike chat reply successful'})

class GetAllIdLikeChatItem(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        wishlist = LikeChatItem.objects.filter(user=user)
        chatItems = []
        for item in wishlist:
            chatItem = item.chatitem
            chatItems.append(chatItem)
        
        serializer = IdLikeChatItemSerializer(chatItems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetAllIdLikeChatReply(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        wishlist = LikeChatReply.objects.filter(user=user)
        chatReplies = []
        for item in wishlist:
            chatReply = item.chatreply
            chatReplies.append(chatReply)
        
        serializer = IdLikeChatReplySerializer(chatReplies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetAllIdDislikeChatItem(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        wishlist = DisLikeChatItem.objects.filter(user=user)
        chatItems = []
        for item in wishlist:
            chatItem = item.chatitem
            chatItems.append(chatItem)
        
        serializer = IdDisLikeChatItemSerializer(chatItems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetAllIdDislikeChatReply(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        wishlist = DisLikeChatReply.objects.filter(user=user)
        chatReplies = []
        for item in wishlist:
            chatReply = item.chatreply
            chatReplies.append(chatReply)
        
        serializer = IdDisLikeChatReplySerializer(chatReplies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# ======================================================================================================