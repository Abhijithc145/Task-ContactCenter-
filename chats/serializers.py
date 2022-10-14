from rest_framework import serializers
from .models import *



class organization_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = "__all__"        

# class create_organization_Serializer(serializers.ModelSerializer):

#     class Meta:
#         model = Organizations
#         fields = "__all__"   

class department_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = "__all__" 
                      
    # organization = organization_Serializer(read_only=True)


class agent_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Agent_Model
        fields = "__all__"     


class bot_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bot_Model
        fields = "__all__"          