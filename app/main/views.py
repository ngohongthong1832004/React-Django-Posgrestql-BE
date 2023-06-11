from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Film
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

## API
from main.serializers import FilmSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework import permissions
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from django.views.generic.edit import FormView
from .forms import MyForm


from .forms import *

class LoginView( FormView) :
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
        
        # return super().form_valid(form)




class LoginAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]


    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user is not None:
            # User credentials are valid
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # User credentials are invalid
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)









class FilmApiView(APIView):
    # Uncomment the line below to apply the desired permission class or classes
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        films = Film.objects.all()


        film = films.filter(id=kwargs['id'])
        serializer = FilmSerializer(film, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)







def home(request):
    return HttpResponse("Hello world! my friends")


def default(request):
    test = {
        "name": "test",
        "age": 20,
        "children": "[{name: 'test1', age: 10}, {name: 'test2', age: 20}]"
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
    
    # def get(self, *args, **kwargs):
    #     last_film = self.model.objects.get(id=4)
    #     response = HttpResponse({
    #         last_film.name,
    #         last_film.casts,
    #         last_film.desc,
    #         last_film.year,
    #         }
    #     )
        
    #     return response
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["book_list"] = Film.objects.all()
        return context
    


class FilmListView(LoginRequiredMixin, ListView):
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    model = Film
    template_name = 'home.html'
    context_object_name = 'film_list'
    # ordering = ['-id']
    # paginate_by = 5
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
    # context_object_name = 'film'
    # def get(self, *args, **kwargs):
    #     film = self.model.objects.get(id=kwargs['pk'])
    #     response = HttpResponse({
    #         film.name,
    #         film.casts,
    #         film.desc,
    #         film.year,
    #         }
    #     )
        
    #     return response
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
        # Process the form data
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        # Perform actions with the form data (e.g., save to database)
        # ...
        print(name, email, message)
        # Redirect to a new URL:

        return super().form_valid(form)





    