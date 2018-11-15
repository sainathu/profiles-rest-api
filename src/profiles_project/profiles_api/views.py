from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
class HelloApiView(APIView):
     """Test API View"""

     serializer_class = serializers.HelloSerializer

     def get(self, request, format=None):
         an_apiview = [  'Uses HTTP methods as functions',
                         'Hello my name is borat',
                         'Lorem ipsum']

         return Response({'message': 'Hello', 'content': an_apiview})

     def post(self, request):
         """Create hello message with name"""
         serializer = serializers.HelloSerializer(data=request.data)

         if serializer.is_valid():
             name = serializer.data.get('name')
             message = 'Hello {0}'.format(name) #para mais: 0, 1, 2, 3...
             return Response({'message': message})
         else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     def put(self, request, pk=None):
         """Updates the object"""
         return Response({'method': 'put'})

     def patch(self, request, pk=None):
         """Updates partially the object"""
         return Response({'method': 'patch'})

     def delete(self, request, pk=None):
         """Deletes the object"""
         return Response({'method': 'delete'})
