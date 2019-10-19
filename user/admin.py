from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.DepartmentUser)
admin.site.register(models.CitizenUser)
