from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django.forms import *

class RegisterForms(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class LoginForms(Form):
    username = CharField(max_length=30,widget=TextInput(attrs={'type':'text', 'placeholder':'username...'}))
    password = CharField(max_length=50,widget=PasswordInput(attrs=dict(type='password',placeholder='password...')))