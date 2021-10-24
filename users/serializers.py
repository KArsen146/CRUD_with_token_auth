from .models import UserToken
from rest_framework import serializers


class UserTokenSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = UserToken.objects.create_user(**validated_data)
        return user

    class Meta:
        model = UserToken
        fields = '__all__'
