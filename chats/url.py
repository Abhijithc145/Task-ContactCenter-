from django.urls import path,include
from .import views
from .views import *
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path("chat_organizations/",OrganizationsList.as_view(),name="chat_organizations"),
    path("chat/<uuid:pk>",organizationDetails.as_view(),name="chat_organizationslist"),
    path("departments/",DepartmentList.as_view(),name="department_data"),
    path("departments/<uuid:pk>",DepartmentDetails.as_view(),name="department_data"),
    path("agents/",AgentList.as_view(),name="agents"),
    path("agents/<uuid:pk>",AgentDetails.as_view(),name="agents_data"),
    path("bots/",BotList.as_view(),name="bots"),
    path("bots/<uuid:pk>",BotDetails.as_view(),name="bots_data"),
    path("conversations/",ConversationList.as_view(),name="bots"),
    path("conversations/<uuid:pk>",ConversationDetails.as_view(),name="bots_data"),
    path("message/",MessageList.as_view(),name="message_data"),
    path("message/<uuid:pk>",MessageDetails.as_view(),name="bots_data"),
    path("userprofiles/",UserProfileList.as_view(),name="userprofile_data"),
    path("userprofiles/<uuid:pk>",UserProfileDetails.as_view(),name="userprofile_data"),

    
]