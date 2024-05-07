# from django.shortcuts import render
# from.models import CustomUser
# from.serializers import UserSerializer
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class CreateUser(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# class ReadUser(APIView):
#     def get(self, request):
#         users = CustomUser.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

# class UpdateUser(APIView):
#     def put(self, request, pk):
#         user = CustomUser.objects.get(pk=pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# class DeleteUser(APIView):
#     def delete(self, request, pk):
#         user = CustomUser.objects.get(pk=pk)
#         user.delete()
#         return Response({'message': 'User deleted successfully'})

from django.shortcuts import render
# Create your views here.
# users/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from.models import CustomUser
from.serializers import UserSerializer

class CustomUserListView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CustomUserDetailView(APIView):
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response(status=404)

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=204)
