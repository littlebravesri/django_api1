import csv
import sqlite3

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import Type, Dataset
from .serializer import TypeSerializer, DatasetSerializer
# Create your views here.

def index(request):
    return HttpResponse("HEllo World")

class AllTech(ListAPIView):
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
            if serializer.data is "pearson":
                #serializer.save()
                a = 2+9
                return Response(a, status=200)
            else:
                a = 0
                return Response(a, status=200)

            # conn = None
            # conn = sqlite3.connect('db')
            # cur = conn.cursor()
            # cur.execute("SELECT * FROM analysis_dataset")
            #
            # rows = cur.fetchall()
            #
            # for row in rows:
            #     print(row)
            #pearsoncorr = Dataset.corr(method='pearson')
            #return Response(a, status=200) #status.HTTP_201_CREATED    serializer.data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

