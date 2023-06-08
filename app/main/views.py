from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def home(request):
    return HttpResponse("Hello world! my friends")


def default(request):
    return HttpResponse("json")



class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)
    
class MorningGreetingView(GreetingView):
    greeting = "Morning to ya"