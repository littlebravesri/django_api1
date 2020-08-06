import sqlite3

from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from .models import User
from .serializer import UserSerializer
import pandas as pd

# Create your views here.

class AppUserAPI(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @classmethod
    def get_extra_actions(cls):
        return []

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        con = sqlite3.connect("db.sqlite3")
        df = pd.read_sql_query("SELECT username, currentPassword from app_user_user", con)
        con.close()

        if serializer.is_valid():
            try:
                queryset = User.objects.get(username=serializer.data['username'])
            except User.DoesNotExist:
                return Response("Username does not exist", status=status.HTTP_404_NOT_FOUND)
            serializer = UserSerializer(queryset, data=request.data)
            if serializer.is_valid():
                currPass = df["currentPassword"][df['username'] == serializer.validated_data['username']]
                if serializer.validated_data['currentPassword'] == currPass.item():
                    serializer.validated_data['currentPassword'] = serializer.validated_data['newPassword']
                    serializer.validated_data['newPassword'] = ""
                    serializer.save()
                    return Response("Password changed successfully", status=200)
                else:
                    return Response("Current Password does not match", status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

