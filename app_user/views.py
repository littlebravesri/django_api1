from django.shortcuts import render

import re
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import User
from .serializer import UserSerializer
# Create your views here.

class AppUserAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

