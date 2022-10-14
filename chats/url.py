from django.urls import path,include
from .import views
from .views import *

urlpatterns = [
    path("chat_organizations/",Organizations.as_view(),name="chat_organizations"),
    # path("chat_organizations/<str:uuid>",organization_list.as_view(),name="chat_organizationslist"),
    
]