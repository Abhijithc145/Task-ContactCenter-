from django.urls import path,include
from .import views
from .views import *

urlpatterns = [
    path("chat_organizations/",Organizationss.as_view(),name="chat_organizations"),
    path("chat/<uuid:pk>",organization_list.as_view(),name="chat_organizationslist"),
    
]