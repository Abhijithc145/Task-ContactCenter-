from django.urls import path,include
from .import views
from .views import *
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path("chat_organizations/",OrganizationsList.as_view(),name="chat_organizations"),
    path("chat/<uuid:pk>",organizationDetails.as_view(),name="chat_organizationslist"),
    path("departments/",DepartmentList.as_view(),name="department_data"),
    path("departments/<uuid:pk>",DepartmentDetails.as_view(),name="department_data"),

    
]