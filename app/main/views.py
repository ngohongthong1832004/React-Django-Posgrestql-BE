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

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token



from .models import Film, Movies

from datetime import date

from main.serializers import *

from .forms import *

# CUSTOM pagination
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100



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
        films = Movies.objects.all()
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



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# =====================================================================================================================================
# =====================================================================================================================================
# =====================================================================================================================================
# =====================================================================================================================================

# API RESTFULL

class GetOneData(APIView):
    permission_classes = [IsAuthenticated]
  
    def get(self, request, *args, **kwargs):
        # user = request.user
        return Response({'message': "user.username"})
class GetAllData(APIView):
    permission_classes = [IsAuthenticated]
    model = Movies
    serializer = MovieSerializer(model.objects.all(), many=True)
    def get(self, request, *args, **kwargs):
        paginator = CustomPagination()
        paginated_items = paginator.paginate_queryset(self.serializer.data, request)
        return Response(paginated_items, status=status.HTTP_200_OK)




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
            'user_id': user.pk,
            'email': user.email,
            'isStaff' : user.is_staff
        })


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response({'message': 'Logout successful'})
    

