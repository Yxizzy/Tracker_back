from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tracker, Product, Status

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = ("id", "code", "user")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "vendor", "address", "status", "code", "timestamp")

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ("id", "status", "timestamp")