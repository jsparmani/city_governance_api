from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'department'
router = DefaultRouter()
router.register('departments', views.DepartmentViewset)
router.register('projects', views.ProjectViewset)
router.register('schemes', views.SchemeViewset)

urlpatterns = [
    path('', include(router.urls)),
]
