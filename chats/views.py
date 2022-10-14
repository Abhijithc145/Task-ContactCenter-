from telnetlib import STATUS
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from .models import *

# Create your views here.


class Organizationss(APIView):
    def get(self,request):
        datas = Organizations.objects.all()
        serializers = organization_Serializer(datas,many = True).data
        return Response(serializers,status=status.HTTP_200_OK)


    def post(self,request):
        serializer = organization_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   


class organization_list(APIView):
    def get(self,request,pk = None):

        if pk:
            datas = Organizations.objects.get(id=pk)
            serializer = organization_Serializer(datas)
            return Response({ "data": serializer.data}, status=status.HTTP_200_OK)
 
        datas = Organizations.objects.all()
        serializer = organization_Serializer(datas, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)  


    def put(self,request,pk = None):
        datas = Organizations.objects.get(id=pk)
        serializer = organization_Serializer(datas, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})                   