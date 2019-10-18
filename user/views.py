from django.shortcuts import render
from . import serializers
from rest_framework.settings import api_settings
from rest_framework import generics, mixins, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""

    serializer_class = serializers.UserSerializer


class EditUserView(generics.RetrieveUpdateDestroyAPIView, generics.GenericAPIView):
    """Create a new user in the system"""

    serializer_class = serializers.EditUserSerializer
    queryset = get_user_model().objects.all()


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""

    serializer_class = serializers.AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ListUserView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """See users in the database"""

    serializer_class = serializers.UserListSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )
