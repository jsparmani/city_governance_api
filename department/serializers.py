from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


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


class ComplaintSerializer(serializers.ModelSerializer):
    """Serialize Complaint model"""

    department = serializers.PrimaryKeyRelatedField(
        queryset=models.Department.objects.all()
    )

    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all())

    image = serializers.ImageField()

    class Meta:
        model = models.Complaint
        fields = ('id', 'department', 'user',
                  'title', 'description', 'image')
        read_only_fields = ('id', )


class BillPaymentSerializer(serializers.ModelSerializer):
    """Serialize BillPayment model"""

    department = serializers.PrimaryKeyRelatedField(
        queryset=models.Department.objects.all()
    )

    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all())

    class Meta:
        model = models.BillPayment
        fields = ('id', 'department', 'user', 'reg_no',
                  'payment_id', 'payment_amt', 'time')
        read_only_fields = ('id', 'time')


class ConnectionSerializer(serializers.ModelSerializer):
    """Serialize Connection model"""

    department = serializers.PrimaryKeyRelatedField(
        queryset=models.Department.objects.all()
    )

    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all())

    address_proof = serializers.FileField()

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


    class Meta:
        model = models.Connection
        fields = ('id', 'department', 'user', 'name',
                  'phone_no', 'address', 'address_proof')
        read_only_fields = ('id',)
