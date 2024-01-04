from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserProfileSerializer, UserSerializer
from rest_framework import status
# Create your views here.

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "success": True,
            "message": "User List",
            "data": serializer.data
        })
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": status.HTTP_201_CREATED, # "status": "201
                "success": True,
                "message": "User Created",
                "data": serializer.data
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "User not created",
            "data": serializer.errors
        })
    
    def delete(self, request):
        user = User.objects.get(pk=request.data['id'])
        if user:
            user.delete()
            return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "User Deleted",
                "data": []
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "User not found",
            "data": []
        })
    
class UserOneView(APIView):
    def get(self, request):
        user = User.objects.get(id=request.GET.get('id'))
        if user:
            serializer = UserSerializer(user)
            return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "User List",
                "data": serializer.data
            })
        
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "User not found",
            "data": []
        })
    


class UserProfileView(APIView):
    def get(self, request):
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "success": True,
            "message": "User List",
            "data": serializer.data
        })
    
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": status.HTTP_201_CREATED,
                "success": True,
                "message": "User Created",
                "data": serializer.data
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "User not created",
            "data": serializer.errors
        })
    
    def delete(self, request):
        user = UserProfile.objects.get(pk=request.data['id'])
        if user:
            user.delete()
            return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "User Deleted",
                "data": []
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "User not found",
            "data": []
        })
    
