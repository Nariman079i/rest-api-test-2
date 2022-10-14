from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render , redirect , HttpResponse
from django.views.generic import *
from rest_framework.generics import *
from .forms import *
from .models import *
from .serializer import *


# Create your views here.

class SityApiView(ListAPIView):
    queryset = Sity.objects.all()
    serializer_class = SitySerializer

class UsersApiView(ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class IndustrialApiView(ListAPIView):
    queryset = Industrial.objects.all()
    serializer_class = IndustrialSerializer

def index(requests):
    context = dict()
    if requests.user.is_authenticated:
        data = {
            'username': requests.user.username,
            'password': requests.user.password,
            'email': requests.user.email
        }
        context['data'] = data
    else:
        data = {
            'Registrarion': "{% url  'register' %}",
            'Login': "{% url 'login' %}"
                }
        context['data'] = data
    file = 'main/index.html'
    return render(requests, file, context=context)

def register_user(requests):
    if requests.user.is_authenticated:
        return redirect('login')
    else:
        if requests.method == 'POST':
            form = RegisterForms(requests.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                email_ = form.cleaned_data['email']
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                user = User.objects.create_user(
                    username=username,
                    email=email_,
                    password=password1,
                )
                user.save()
                auth_user = authenticate(requests,username=username, password=password1)
                login(requests,auth_user)
                return redirect('main')
        else:
            form = RegisterForms()
            file = 'main/register.html'
            return render(requests,file,context=dict(form=form))
def login_user(requests):
    if requests.user.is_authenticated:
        return redirect('main')
    else:
        if requests.method == 'POST':
            form = LoginForms(requests.POST)
            if form.is_valid():
                info = form.cleaned_data
                username = info['username']
                password = info['password']
                user = authenticate(requests, username=username,password=password)
                if user is not None:
                    login(requests, user)
                    return redirect('main')
                else:
                    pass
        else:
            form = LoginForms()
            file = 'main/login.html'
            context = dict(form=form)
            return render(requests,file , context=context)
def logout_user(requests):
    if requests.user.is_authenticated:
        logout(requests)
        return redirect('login')
    else:
        return redirect('login')