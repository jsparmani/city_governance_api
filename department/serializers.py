from rest_framework import serializers
from . import models


class DepartmentSerializer(serializers.ModelSerializer):
    """Serialize Department model"""

    class Meta:
        model = models.Department
        fields = ('id', 'department_name',
                  'department_description', 'department_head_name', 'department_head_phone', 'department_email')
        read_only_fields = ('id', )
