from django.db import models

# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=255)
    department_description = models.TextField()
    department_head_name = models.CharField(max_length=255)
    department_head_phone = models.PositiveIntegerField()
    department_email = models.EmailField()

    def __str__(self):
        return self.department_name
