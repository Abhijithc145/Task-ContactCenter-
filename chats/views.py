from telnetlib import STATUS
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from .models import *
from django.shortcuts import render,get_object_or_404
import datetime
from rest_framework import viewsets
# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


# organization CRUD

class OrganizationsList(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Organization.objects.filter(is_active = True)
    serializer_class = organization_Serializer
    def get(self,request,*args,**kwargs):
        
        return self.list(request,*args,**kwargs)  

    def post(self,request,*args,**kwargs):
        
        return self.create(request,*args,**kwargs) 


class organizationDetails(APIView):
    def get(self,request,pk = None):

        if pk:
            try:
                datas = Organization.objects.get(id=pk,is_active = True)
                serializer = organization_Serializer(datas)
                return Response({ "data": serializer.data}, status=status.HTTP_200_OK)
            except:
                return Response({"Error":"The data is no here"})    
 
        datas = Organization.objects.all()
        serializer = organization_Serializer(datas, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)  


    def put(self,request,pk = None):
        try:
            datas = Organization.objects.get(id=pk)
            serializer = organization_Serializer(datas, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors})   
        except:
                return Response({"Error":"The data is no here"})          

    def delete(self,request,pk = None):
        data = get_object_or_404(Organization, id = pk)
        data.is_active = not(data.is_active)
        data.deleted_at =datetime.datetime.now() 
        data.save()
        return Response({"status": "success", "data": "student Deleted"})                    



#       Department CRUD

class DepartmentList(APIView):
    def get(self,request):
        datas = Department.objects.filter(is_active = True)
        serializer =department_Serializer(datas,many=True)
        return Response(serializer.data)  
        
    def post(self,request):
        try:
            # org_id = request.data.get('organization')
            # org =  organization_Serializer(Organization.objects.get(id=org_id)).data['id']
            # request.data['organization'] = org
            # print(org)
            # print(request.data['organization'],"----------------------------")
            # # print(request.data,"lllllllllllllllllllllllll")
            # print("request", request.data)
            serializer = department_Serializer(data=request.data)
            if serializer.is_valid():   
                serializer.save()
                print(serializer)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)    
        except Exception as err:
            print(err)
            return Response("ERR")  



class DepartmentDetails(APIView):
    def get(self,request,pk):
        try:
            datas = Department.objects.get(id=pk,is_active = True)
            serilizer = department_Serializer(datas)
            return Response({ "data": serilizer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  

    def put(self,request,pk):
        try:
            datas = Department.objects.get(id=pk,is_active = True)
            serializer = department_Serializer(datas, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors}) 
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  


    def delete(self,request,pk):
        try:
            data = get_object_or_404(Department, id = pk)
            data.is_active = not(data.is_active)
            data.deleted_at =datetime.datetime.now() 
            data.save()
            return Response({"status": "success", "data": "student Deleted"}) 
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  
        



class AgentList(APIView):
    def get(self,request):
        datas = Agent_Model.objects.filter(is_active = True)
        serializer =agent_Serializer(datas,many=True)
        return Response(serializer.data)  
        
    def post(self,request):
        try:
     
            serializer = agent_Serializer(data=request.data)
            if serializer.is_valid():   
                serializer.save()
                print(serializer)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)    
        except Exception as err:
            print(err)
            return Response("ERR")  


class AgentDetails(APIView):   
    def get(self,request,pk):
        try:
            datas = Agent_Model.objects.get(id=pk,is_active = True)
            serilizer = agent_Serializer(datas)
            return Response({ "data": serilizer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  

    def put(self,request,pk):
        try:
            datas = Agent_Model.objects.get(id=pk,is_active = True)
            serializer = agent_Serializer(datas, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors}) 
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  


    def delete(self,request,pk):
        try:
            data = get_object_or_404(Agent_Model, id = pk)
            data.is_active = not(data.is_active)
            data.deleted_at =datetime.datetime.now() 
            data.save()
            return Response({"status": "success", "data": "student Deleted"}) 
        except Exception as err:
            print(err)         



class BotList(APIView):
    def get(self,request):
        datas = Bot_Model.objects.filter(is_active = True)
        serializer =bot_Serializer(datas,many=True)
        return Response(serializer.data)  
        
    def post(self,request):
        try:
     
            serializer = bot_Serializer(data=request.data)
            if serializer.is_valid():   
                serializer.save()
                print(serializer)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)    
        except Exception as err:
            print(err)
            return Response("ERR")              


class BotDetails(APIView):   
    def get(self,request,pk):
        try:
            datas = Bot_Model.objects.get(id=pk,is_active = True)
            serilizer = bot_Serializer(datas)
            return Response({ "data": serilizer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  

    def put(self,request,pk):
        try:
            datas = Bot_Model.objects.get(id=pk,is_active = True)
            serializer = bot_Serializer(datas, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors}) 
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  


    def delete(self,request,pk):
        try:
            data = get_object_or_404(Bot_Model, id = pk)
            data.is_active = not(data.is_active)
            data.deleted_at =datetime.datetime.now() 
            data.save()
            return Response({"status": "success", "data": "student Deleted"}) 
        except Exception as err:
            print(err)         

class ConversationList(APIView):
    def get(self,request):
        datas = Conversations_Model.objects.filter(is_active = True)
        serializer =conversation_Serializer(datas,many=True)
        return Response(serializer.data)  
        
    def post(self,request):
        print(request.data,";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        try:
     
            serializer = conversation_Serializer(data=request.data)
            if serializer.is_valid():   
                serializer.save()
                print(serializer)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)    
        except Exception as err:
            print(err)
            return Response("ERR")     


class ConversationDetails(APIView):   
    def get(self,request,pk):
        try:
            datas = Conversations_Model.objects.get(id=pk,is_active = True)
            serilizer = conversation_Serializer(datas)
            return Response({ "data": serilizer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  

    def put(self,request,pk):
        try:
            datas = Conversations_Model.objects.get(id=pk,is_active = True)
            serializer = conversation_Serializer(datas, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors}) 
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  


    def delete(self,request,pk):
        try:
            data = get_object_or_404(Conversations_Model, id = pk)
            data.is_active = not(data.is_active)
            data.deleted_at =datetime.datetime.now() 
            data.save()
            return Response({"status": "success", "data": "student Deleted"}) 
        except Exception as err:
            print(err)  


class MessageList(APIView):
    def get(self,request):
        datas =Message_Module.objects.filter(is_active = True)
        serializer =message_Serializer(datas,many=True)
        return Response(serializer.data)  
        
    def post(self,request):
        print(request.data,";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        try:
     
            serializer = message_Serializer(data=request.data)
            if serializer.is_valid():   
                serializer.save()
                print(serializer)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)    
        except Exception as err:
            print(err)
            return Response("ERR")     


class MessageDetails(APIView):   
    def get(self,request,pk):
        try:
            datas = Message_Module.objects.get(id=pk,is_active = True)
            serilizer = message_Serializer(datas)
            return Response({ "data": serilizer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  

    def put(self,request,pk):
        try:
            datas = Message_Module.objects.get(id=pk,is_active = True)
            serializer = message_Serializer(datas, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors}) 
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  


    def delete(self,request,pk):
        try:
            data = get_object_or_404(Message_Module, id = pk)
            data.is_active = not(data.is_active)
            data.deleted_at =datetime.datetime.now() 
            data.save()
            return Response({"status": "success", "data": "student Deleted"}) 
        except Exception as err:
            print(err)  


class UserProfileList(APIView):
    def get(self,request):
        datas =UserProfile_Module.objects.filter(is_active = True)
        serializer =userprofile_Serializer(datas,many=True)
        return Response(serializer.data)  
        
    def post(self,request):
        print(request.data,";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        try:
     
            serializer = userprofile_Serializer(data=request.data)
            if serializer.is_valid():   
                serializer.save()
                print(serializer)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)    
        except Exception as err:
            print(err)
            return Response("ERR")   




class UserProfileDetails(APIView):   
    def get(self,request,pk):
        try:
            datas = UserProfile_Module.objects.get(id=pk,is_active = True)
            serilizer = userprofile_Serializer(datas)
            return Response({ "data": serilizer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  

    def put(self,request,pk):
        try:
            datas = UserProfile_Module.objects.get(id=pk,is_active = True)
            serializer = userprofile_Serializer(datas, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors}) 
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  


    def delete(self,request,pk):
        try:
            data = get_object_or_404(UserProfile_Module, id = pk)
            data.is_active = not(data.is_active)
            data.deleted_at =datetime.datetime.now() 
            data.save()
            return Response({"status": "success", "data": "student Deleted"}) 
        except Exception as err:
            print(err)  

            


class ChannelList(APIView):
    def get(self,request):
        datas =Channel_Model.objects.filter(is_active = True)
        serializer =channel_Serializer(datas,many=True)
        return Response(serializer.data)  
        
    def post(self,request):
        print(request.data,";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        try:
     
            serializer = channel_Serializer(data=request.data)
            if serializer.is_valid():   
                serializer.save()
                print(serializer)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)    
        except Exception as err:
            print(err)
            return Response("ERR")            


#             

class ChannelDetails(APIView):   
    def get(self,request,pk):
        try:
            datas = Channel_Model.objects.get(id=pk,is_active = True)
            serilizer = channel_Serializer(datas)
            return Response({ "data": serilizer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  

    def put(self,request,pk):
        try:
            datas = Channel_Model.objects.get(id=pk,is_active = True)
            serializer = channel_Serializer(datas, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors}) 
        except Exception as err:
            print(err)
            return Response({"Error":"Error"})  


    def delete(self,request,pk):
        try:
            data = get_object_or_404(Channel_Model, id = pk)
            data.is_active = not(data.is_active)
            data.deleted_at =datetime.datetime.now() 
            data.save()
            return Response({"status": "success", "data": "student Deleted"}) 
        except Exception as err:
            print(err)  

            