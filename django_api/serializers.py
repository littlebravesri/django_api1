from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ItemListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemList
        fields = ['id', 'status', 'type', 'name', 'city']


class ExampleModelLessSerializer(serializers.Serializer):
    project_name = serializers.CharField()
    total_head_count = serializers.IntegerField()
    start_date = serializers.DateTimeField()
    location = serializers.CharField()





