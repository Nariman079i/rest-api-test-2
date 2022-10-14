from rest_framework.serializers import *

from .models import *


class SitySerializer(ModelSerializer):
    class Meta:
        model = Sity
        fields = '__all__'


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class IndustrialSerializer(ModelSerializer):
    class Meta:
        model = Industrial
        fields = '__all__'
