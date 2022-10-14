from django.contrib import admin
from django.urls import path , include

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/v1/locate/', SityApiView.as_view()),
    path('api/v1/user/',UsersApiView.as_view() ),
    path('api/v1/industrial/', UsersApiView.as_view())
]
