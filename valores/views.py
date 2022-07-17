from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

from valores.models import valores_modelo
from valores.serializers import valores_serializer, valores_ambiente_serializer, valores_suelo_serializer, valores_agua_serializer

class valores_viewAll(APIView):
    def custom_response(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        response = json.loads(res)
        return response

    def get(self, request, format=None):
        queryset = valores_modelo.objects.all()
        serializer = valores_serializer(queryset , many=True, context={'request':request})
        return Response(self.custom_response("Success", serializer.data, status=status.HTTP_200_OK))

    def post(self, request):
        serializer = valores_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(self.custom_response("Success", serializer.data, status=status.HTTP_201_CREATED))
        return Response(self.custom_response("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))

class valores_viewAmbiente(APIView):
    def get(self, request, format=None):
        queryset = valores_modelo.objects.all()
        serializer = valores_ambiente_serializer(queryset , many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class valores_viewSuelo(APIView):
    def get(self, request, format=None):
        queryset = valores_modelo.objects.all()
        serializer = valores_suelo_serializer(queryset , many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class valores_viewAgua(APIView):
    def get(self, request, format=None):
        queryset = valores_modelo.objects.all()
        serializer = valores_agua_serializer(queryset , many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)