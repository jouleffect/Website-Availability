from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from sites.models import SiteAvail
from sites.api.serializers import SiteAvailSerializer
from sites.api import responses


class IndexView(APIView):

    def get(self,request):

        sites = SiteAvail.objects.all()
        serializer = SiteAvailSerializer(sites, many=True)
        return Response(serializer.data)

class UrlAPIView(APIView):
    
    def get(self,request,url):  

        response = responses.get_content(url)
        serializer = SiteAvailSerializer(data=response)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         
        

class UrlRegexAPIView(APIView):

    def get(self,request,url,regex):        

        response = responses.get_content(url,regex)
        serializer = SiteAvailSerializer(data=response)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)