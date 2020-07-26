import re
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import Type, Dataset
from .serializer import TypeSerializer, DatasetSerializer
# Create your views here.

def index(request):
    return HttpResponse("HEllo World")

class ModelLessAPI(ListAPIView):
    queryset = Type.objects.all() #filter(correlation="pearson")
    serializer_class = TypeSerializer

    # dataset = Dataset()
    #
    # dataReader = csv.reader(open('analysis/product_a.csv'), delimiter=',', quotechar='"')
    # for row in dataReader:
    #     dataset.date_w = row[1]
    #     dataset.price = row[2]
    #     dataset.total_vol = row[3]
    #     dataset.plu1 = row[4]
    #     dataset.plu2 = row[5]
    #     dataset.plu3 = row[6]
    #     dataset.bags_t = row[7]
    #     dataset.bags_s = row[8]
    #     dataset.bags_l = row[9]
    #     dataset.bags_lx = row[10]
    #     dataset.type = row[11]
    #     dataset.year = row[12]
    #     dataset.location = row[13]
    #     dataset.save()

    def post(self, request, format=None):
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid():
            x = re.search("pearson", str(serializer.data))
            if x:
                return Response("pearson", status=200)
            else:
                return Response("spearman", status=200)
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