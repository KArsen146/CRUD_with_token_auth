from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from users.models import UserToken
from users.serializers import UserTokenSerializer
from rest_framework.permissions import IsAuthenticated


class UserTokenViewSet(ModelViewSet):
    serializer_class = UserTokenSerializer
    queryset = UserToken.objects.all()
    permission_classes = (IsAuthenticated, )
