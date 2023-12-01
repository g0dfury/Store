from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import mixins

from django.contrib.auth.models import User

from .serializer import *

class UserViewSet(GenericViewSet, mixins.CreateModelMixin, ):
    def get_queryset(self):
        if self.action == 'retrieve':
            return User.objects.get(id=self.request.user.id)
        return User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action == 'retrieve':
            return UserSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)