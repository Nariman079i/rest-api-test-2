from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render , redirect , HttpResponse
from django.db.models import *
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
        chat = {
            'users': User.objects.all()
        }
        context['data'] = data
        context.update(**chat)
    else:
        data = {
            'Registrarion': "{% url  'register' %}",
            'Login': "{% url 'login' %}"
                }
        context['data'] = data
    file = 'main/index.html'
    return render(requests, file, context=context)

def chat(requests, user_id):
    context = dict()
    if not requests.user.is_authenticated:
        return redirect('login')
    else:
        data = {
            'doner': requests.user,
            'recip': User.objects.get(pk=user_id),
            'messages': Chat.objects.filter(Q(doner=requests.user) | Q(doner__pk=user_id) , Q(recip=requests.user) | Q(recip__pk=user_id))
        }
        context.update(**data)
        if requests.method == 'POST':
            form = SendMessage(requests.POST)
            if form.is_valid():
                mess = form.cleaned_data['message']
                Chat.objects.create(doner=requests.user,recip=context['recip'] , message=mess)
                return redirect('chat',user_id=user_id)
        else:
            context['form'] = SendMessage()
            file = 'main/chat.html'
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
                try:
                    user = User.objects.create_user(
                        username=username,
                        email=email_,
                        password=password1,
                    )
                    user.save()
                    auth_user = authenticate(requests,username=username, password=password1)
                    login(requests,auth_user)
                except:
                    form.error_messages("Password error!")
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