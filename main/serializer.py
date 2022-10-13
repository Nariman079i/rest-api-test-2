from rest_framework.serializers import *

from .models import Sity


class SitySerializer(ModelSerializer):
    class Meta:
        model = Sity
        fields = '__all__'