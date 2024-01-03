from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from uuid import uuid4
from .serializers import UrlModelSerializer
from .models import UrlModel
from rest_framework import status
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

class UrlShortnerView(APIView):
    def get(self, request, pk):

        urlData = get_object_or_404(UrlModel, uuid=pk)

        url = urlData.url

        if url == None:
            return Response({'message': 'URL Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        print(url, pk)

        if "https" in url:
            return redirect(url)
        else:
            return redirect('https://' + url)
    
    def post(self, request):
        
        userData = request.data

        url = userData.get('url')
        genUuid = str(uuid4())[:5]

        data = {
            'url': url,
            'uuid': genUuid
        }

        urlModelSerializer = UrlModelSerializer(data=data)

        if urlModelSerializer.is_valid():
            urlModelSerializer.save()
            newUrl = 'https://localhost:8000/' + genUuid
            return Response({'message': 'URL Shortened Successfully', 'url': newUrl, 'status': status.HTTP_201_CREATED})
        
        return Response({'message': urlModelSerializer.errors, 'status': status.HTTP_400_BAD_REQUEST})
