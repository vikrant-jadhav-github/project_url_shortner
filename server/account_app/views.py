from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VisitorModelSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import VisitorModel
from rest_framework.permissions import IsAuthenticated

def getToken(User):
    genToken = RefreshToken.for_user(User)
    return {
        'refresh': str(genToken),
        'access': str(genToken.access_token)
    }

class RegisterView(APIView):
    def post(self, request):
        userData = request.data
        visitorModelSerializer = VisitorModelSerializer(data=userData)
        if visitorModelSerializer.is_valid():
            visitor = visitorModelSerializer.save()
            token = getToken(visitor)
            return Response({'message': 'User Created', 'token': token, 'data': visitorModelSerializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': visitorModelSerializer.errors, 'status': status.HTTP_400_BAD_REQUEST})
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        visitorData = get_object_or_404(VisitorModel, pk=user.id)
        visitorModelSerializer = VisitorModelSerializer(visitorData)
        return Response({'message': 'User Data Retrieved', 'data': visitorModelSerializer.data}, status=status.HTTP_200_OK)