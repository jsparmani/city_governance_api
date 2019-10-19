from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'department'
router = DefaultRouter()
router.register('departments', views.DepartmentViewset)
router.register('projects', views.ProjectViewset)
router.register('schemes', views.SchemeViewset)
router.register('complaints', views.ComplaintViewset)
router.register('downloads', views.FilesViewset)
router.register('payments', views.BillPaymentViewset)

urlpatterns = [
    path('', include(router.urls)),
]
