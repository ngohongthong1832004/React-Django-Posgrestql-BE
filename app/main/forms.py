from django import forms
from .models import *

class MyForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Enter your email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'input', 'placeholder': 'Enter your message'}))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter your pass'}))


 
 
class HotelForm(forms.ModelForm):
 
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']