from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from users.models import UserToken
from users.permissions import IsAuthenticatedWithoutCreate
from users.serializers import UserTokenSerializer


class UserTokenViewSet(ModelViewSet):
    serializer_class = UserTokenSerializer
    queryset = UserToken.objects.all()
    permission_classes = (IsAuthenticatedWithoutCreate, )


