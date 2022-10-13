from django.shortcuts import render
from rest_framework.generics import *
from .models import Sity
from main.serializer import SitySerializer


# Create your views here.

class SityApiView(ListAPIView):
    queryset = Sity.objects.all()
    serializer_class = SitySerializer

