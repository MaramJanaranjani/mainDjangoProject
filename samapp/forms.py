from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    Address = forms.CharField(max_length=100)
    Mob    = forms.CharField(max_length=100)
    
   
class SignUpForm(UserCreationForm):
    Mobile_No = forms.CharField(max_length=10,required  = False, help_text = 'Optional.')

class Meta:
    model = User
    fields = ('username', 'Mobile_No','password1', 'password2', )

class CountClothes(forms.Form):
   
    NumberOfsareesIroning       = forms.CharField(max_length=100)
    NumberOfsareesWashing       = forms.CharField(max_length=100)
    NumberOfshirtsWashing       = forms.CharField(max_length=100)
    NumberOfshirtsIroning       = forms.CharField(max_length=100)
    NumberOftrousersWashing     = forms.CharField(max_length=100)
    NumberOfkidswearWashing     = forms.CharField(max_length=100)
    NumberOftrousersIroning     = forms.CharField(max_length=100)
    NumberOfkidswearIroning     = forms.CharField(max_length=100)
    NumberOfsareesDrycleaning   = forms.CharField(max_length=100)
    NumberOfshirtsDrycleaning   = forms.CharField(max_length=100)    
    NumberOftrousersDrycleaning = forms.CharField(max_length=100)
    NumberOfkidswearDrycleaning = forms.CharField(max_length=100)
    
