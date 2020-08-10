import re
import sqlite3
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from rest_framework.generics import ListAPIView
from .models import Type, Dataset
from .serializer import TypeSerializer, DatasetSerializer
import pandas as pd


# Create your views here.

"""
Model-less API to perform finding the correlation
Model-Based API to GET, PUT, POST and DELETE rows into the database
"""

class ModelLessAPI(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    @classmethod
    def get_extra_actions(cls):
        return []

    def post(self, request):
        serializer = TypeSerializer(data=request.data)

        con = sqlite3.connect("db.sqlite3")
        df = pd.read_sql_query("SELECT * from analysis_dataset", con)
        con.close()

        if serializer.is_valid():
            x = re.search("pearson", str(serializer.data))
            if re.search("pearson", str(serializer.data)):
                pearson = df.corr(method='pearson')
                return render(pearson, 'correlation.html', {'correlation': pearson})
               # return HttpResponse([str(pearson), "Pearson Correlation"], status=status.HTTP_202_ACCEPTED, content_type="application/json")
            elif re.search("spearman", str(serializer.data)):
                spearman = df.corr(method='spearman')
                return HttpResponse([str(spearman), "Spearman Correlation"], status=status.HTTP_202_ACCEPTED, content_type="text/json")
            else:
                Response("Invalid Correlation", status=status.HTTP_400_BAD_REQUEST)
        return Response("Invalid Correlation", status=status.HTTP_400_BAD_REQUEST)



class ModelBasedAPI(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    @classmethod
    def get_extra_actions(cls):
        return []

    def post(self, request):
        serializer = DatasetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ModelBasedAPI_ID(ListAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    def post(self, request):
        serializer = DatasetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, id):
        try:
            model = Dataset.objects.get(id=id)
        except Dataset.DoesNotExist:
            return Response("Product not found", status=status.HTTP_404_NOT_FOUND)
        serializer = DatasetSerializer(model)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id):
        try:
            queryset = Dataset.objects.get(id=id)
        except Dataset.DoesNotExist:
            return Response("Product does not exist", status=status.HTTP_404_NOT_FOUND)
        serializer = DatasetSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, instance, id):
        try:
            queryset = Dataset.objects.get(id=id)
        except Dataset.DoesNotExist:
            return Response("Product does not exist", status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

