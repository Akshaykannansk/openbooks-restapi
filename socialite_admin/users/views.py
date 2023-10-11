from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import status
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .utils import get_tokens_for_user
from .serializers import RegistrationSerializer,userserializer
from django.contrib.auth.models import User
from django.http import JsonResponse 
import json

#, PasswordChangeSerializer

class LoginView(APIView):
    def post(self, request):
        if 'username' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

      
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)
    
class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class userlist(APIView):
    def get(self, request):
        users = User.objects.values('id','username','first_name','last_name','email')
        serializer = userserializer(users,many=True)
        return JsonResponse(serializer.data, safe=False)

class userdetail(APIView):
    def get(self,request,pk ):
        try:
            user = User.objects.get(pk=pk)
        except:
            return HttpResponse(status=404)
        if user:
            serializer = userserializer(user)
            return JsonResponse(serializer.data, safe=False)
        else:
            return HttpResponse(status=404)
    def post(self,request,pk ):
        try:
            user = User.objects.get(pk=pk)
        except:
            return HttpResponse(status=404)
        data = json.dumps(request.data)
        serializer = userserializer(user)
        print(serializer)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)