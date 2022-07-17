from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

from riego.models import riego_modelo
from riego.serializers import riego_serializer

class riego_viewAll(APIView):
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
        queryset = riego_modelo.objects.all()
        serializer = riego_serializer(queryset , many=True, context={'request':request})
        return Response(self.custom_response("Success", serializer.data, status=status.HTTP_200_OK))

    def post(self, request):
        serializer = riego_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(self.custom_response("Success", serializer.data, status=status.HTTP_201_CREATED))
        return Response(self.custom_response("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))