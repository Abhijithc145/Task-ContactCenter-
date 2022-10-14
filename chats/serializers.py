from rest_framework import serializers
from .models import *



class organization_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Organizations
        fields = "__all__"        



class department_Serializer(serializers.ModelSerializer):
    organization = organization_Serializer()
    
    class Meta:
        model = Department
        fields = "__all__"                