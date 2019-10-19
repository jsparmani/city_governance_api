from django.shortcuts import render
from . import serializers
from rest_framework.settings import api_settings
from rest_framework import generics, mixins, viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from . import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.authtoken.models import Token


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


class DepartmentUserViewset(viewsets.ModelViewSet):
    """Manage department users in the database"""

    serializer_class = serializers.DepartmentUserSerializer
    queryset = models.DepartmentUser.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )


class CitizenUserViewset(viewsets.ModelViewSet):
    """Manage citizen users in the database"""

    serializer_class = serializers.CitizenUserSerializer
    queryset = models.CitizenUser.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )


@api_view(['POST'])
def check_user_status(request):
    if request.method == 'POST':
        try:
            user = Token.objects.get(key=request.data['token']).user
            if (user.is_superuser):
                return Response({"type": "superuser"})
            else:
                citizen_usernames = []
                for u in models.CitizenUser.objects.all():
                    citizen_usernames.append(u.user.username)
                department_usernames = []
                for u in models.DepartmentUser.objects.all():
                    department_usernames.append(u.user.username)
                if user.username in citizen_usernames:
                    return Response({"type": "citizen"})
                elif user.username in department_usernames:
                    dept = models.DepartmentUser.objects.get(
                        user__username__exact=user.username).department
                    return Response({"type": "department", "department": dept.department_name, "department_id": dept.id})
            return JsonResponse(request.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
