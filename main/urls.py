
from django.urls import path

from main.views import *

urlpatterns = [
    path('', index, name='main'),
    path('chat/<int:user_id>/', chat , name='chat'),
    path('login/' , login_user , name='login' ),
    path('register/' , register_user , name='register'),
    path('logout/', logout_user, name='logout' )
]
