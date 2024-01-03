from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class VisitorView(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to URL Shortner', 'status': status.HTTP_200_OK})