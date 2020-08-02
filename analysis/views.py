import re, csv
import sqlite3

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import Type, Dataset
from .serializer import TypeSerializer, DatasetSerializer
import pandas as pd

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

class ModelLessAPI(ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    def post(self, request, format=None):
        content_type = 'application/xml'
        serializer = TypeSerializer(data=request.data)

        con = sqlite3.connect("db.sqlite3")
        df = pd.read_sql_query("SELECT * from analysis_dataset", con)
        con.close()

        if serializer.is_valid():
            x = re.search("pearson", str(serializer.data))
            if x:
                pearson = df.corr(method='pearson')
                return Response(pearson, status=200)
            else:
                spearman = df.corr(method='spearman')
                return Response(spearman, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ModelBasedAPI(ListAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    def post(self, request):
        serializer = DatasetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ModelBasedAPI_ID(ListAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer


    def post(self, request):
        serializer = DatasetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, id):
        try:
            model = Dataset.objects.get(id=id)
        except Dataset.DoesNotExist:
            return Response("Product not found")
        serializer = DatasetSerializer(model)
        return Response(serializer.data)


    def put(self, request, id):
        try:
            queryset = Dataset.objects.get(id=id)
        except Dataset.DoesNotExist:
            return Response("Product does not exist", status=status.HTTP_404_NOT_FOUND)
        serializer = DatasetSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, instance, id):
        try:
            queryset = Dataset.objects.get(id=id)
        except Dataset.DoesNotExist:
            return Response("Product does not exist", status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
