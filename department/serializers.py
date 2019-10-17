from rest_framework import serializers
from . import models


class DepartmentSerializer(serializers.ModelSerializer):
    """Serialize Department model"""

    class Meta:
        model = models.Department
        fields = ('id', 'department_name',
                  'department_description', 'department_head_name', 'department_head_phone', 'department_email')
        read_only_fields = ('id', )


class ProjectSerializer(serializers.ModelSerializer):
    """Serialize Project model"""

    department = serializers.PrimaryKeyRelatedField(
        queryset=models.Department.objects.all()
    )

    class Meta:
        model = models.Project
        fields = ('id', 'department', 'project_name',
                  'project_description', 'is_upcoming', 'is_ongoing', 'is_completed')
        read_only_fields = ('id', )


class SchemeSerializer(serializers.ModelSerializer):
    """Serialize Scheme model"""

    department = serializers.PrimaryKeyRelatedField(
        queryset=models.Department.objects.all()
    )

    class Meta:
        model = models.Scheme
        fields = ('id', 'department', 'scheme_name',
                  'scheme_description', 'is_upcoming', 'is_ongoing', 'is_completed')
        read_only_fields = ('id', )


class FileSerializer(serializers.ModelSerializer):

    department = serializers.PrimaryKeyRelatedField(
        queryset=models.Department.objects.all()
    )

    class Meta:
        model = models.File
        fields = ('id', 'file_name', 'department', 'file')
        read_only_fields = ('id', )
