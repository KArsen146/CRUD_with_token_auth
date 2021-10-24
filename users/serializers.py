from django.contrib.auth.hashers import make_password

from .models import UserToken
from rest_framework import serializers


class UserTokenSerializer(serializers.ModelSerializer):
    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = UserToken
        fields = '__all__'
