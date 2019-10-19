from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    department_name = models.CharField(max_length=255)
    department_description = models.TextField()
    department_head_name = models.CharField(max_length=255)
    department_head_phone = models.PositiveIntegerField()
    department_email = models.EmailField()

    def __str__(self):
        return self.department_name


class Project(models.Model):

    department = models.ForeignKey(
        'department.Department', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    project_description = models.TextField()
    is_upcoming = models.BooleanField()
    is_ongoing = models.BooleanField()
    is_completed = models.BooleanField()

    def __str__(self):
        return self.project_name


class Scheme(models.Model):

    department = models.ForeignKey(
        'department.Department', on_delete=models.CASCADE)
    scheme_name = models.CharField(max_length=255)
    scheme_description = models.TextField()
    is_upcoming = models.BooleanField()
    is_ongoing = models.BooleanField()
    is_completed = models.BooleanField()

    def __str__(self):
        return f'{self.scheme_name}--{self.department.department_name}'


class File(models.Model):

    file_name = models.CharField(max_length=255)
    department = models.ForeignKey(
        'department.Department', on_delete=models.CASCADE)
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return f'{self.file_name}--{self.department.department_name}'


class Complaint(models.Model):

    department = models.ForeignKey(
        'department.Department', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='complaint-images/', blank=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.department}--{self.user.username}'


class BillPayment(models.Model):

    department = models.ForeignKey(
        'department.Department', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255)
    payment_amt = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.department}--{self.user}--{self.time}'
