from django.db import models
from django.conf import settings
# Create your models here.


class DepartmentUser(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    department = models.OneToOneField(
        'department.Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class CitizenUser(models.Model):
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username