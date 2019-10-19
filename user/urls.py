from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.ListUserView)
router.register('department-users', views.DepartmentUserViewset)
router.register('citizen-users', views.CitizenUserViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('edit/<int:pk>/', views.EditUserView.as_view(), name='edit'),
    path('check-user/', views.check_user_status, name='check_user')
]
