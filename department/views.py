from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class DepartmentViewset(viewsets.ModelViewSet):
    """Manage departments in the database"""

    serializer_class = serializers.DepartmentSerializer
    queryset = models.Department.objects.all()


class SchemeViewset(viewsets.ModelViewSet):
    """Manage Scheme in the database"""

    serializer_class = serializers.SchemeSerializer
    queryset = models.Scheme.objects.all()


class ProjectViewset(viewsets.ModelViewSet):
    """Manage Project in the database"""

    serializer_class = serializers.ProjectSerializer
    queryset = models.Project.objects.all()


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    serializer_class = serializers.FileSerializer

    def post(self, request, *args, **kwargs):

        file_serializer = serializers.FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
