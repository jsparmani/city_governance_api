from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Department)
admin.site.register(models.Project)
admin.site.register(models.Scheme)
admin.site.register(models.File)
admin.site.register(models.Complaint)
