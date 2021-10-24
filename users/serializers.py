from .models import UserToken
from rest_framework import serializers


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToken
        fields = '__all__'
