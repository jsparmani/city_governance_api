from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
# Create your views here.


class DepartmentViewset(viewsets.ModelViewSet):
    """Manage departments in the database"""

    serializer_class = serializers.DepartmentSerializer
    queryset = models.Department.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
