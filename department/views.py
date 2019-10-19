from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
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

    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAuthenticated]}

    authentication_classes = (TokenAuthentication, )

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class SchemeViewset(viewsets.ModelViewSet):
    """Manage Scheme in the database"""

    serializer_class = serializers.SchemeSerializer
    queryset = models.Scheme.objects.all()

    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAuthenticated]}

    authentication_classes = (TokenAuthentication, )

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class ProjectViewset(viewsets.ModelViewSet):
    """Manage Project in the database"""

    serializer_class = serializers.ProjectSerializer
    queryset = models.Project.objects.all()

    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAuthenticated]}

    authentication_classes = (TokenAuthentication, )

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    serializer_class = serializers.FileSerializer

    authentication_classes = (TokenAuthentication, )

    def post(self, request, *args, **kwargs):

        file_serializer = serializers.FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComplaintViewset(viewsets.ModelViewSet):
    """Manage Complaints in the database"""

    serializer_class = serializers.ComplaintSerializer
    queryset = models.Complaint.objects.all()

    permission_classes = (IsAuthenticated, )

    authentication_classes = (TokenAuthentication, )
