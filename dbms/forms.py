from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Img,Videos


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    
class Form(forms.ModelForm): 
  
    class Meta: 
        model = Img
        exclude = ('user',)

class VideoForm(forms.ModelForm): 
  
    class Meta: 
        model = Videos
        exclude = ('user',)
    
