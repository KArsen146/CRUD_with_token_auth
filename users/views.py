from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from users.models import UserToken
from users.serializers import UserTokenSerializer
from rest_framework.permissions import IsAuthenticated


class UserTokenViewSet(ModelViewSet):
    class IsAuthenticatedWithoutCreate(IsAuthenticated):

        def has_permission(self, request, view):
            if request.method == 'POST':
                return True
            super().has_permission(request, view)

    serializer_class = UserTokenSerializer
    queryset = UserToken.objects.all()
    permission_classes = (IsAuthenticatedWithoutCreate, )


