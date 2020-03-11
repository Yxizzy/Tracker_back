from django.shortcuts import render
from rest_framework.response import Response
import json
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializer import UserSerializer, TrackerSerializer, ProductSerializer, StatusSerializer
from .models import Tracker, Product, Status


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class= UserSerializer
    queryset = User.objects.all()

    def create(self, validated_data):
        username = json.loads(validated_data.body)['username']
        password = json.loads(validated_data.body)['password']
        print(username)
        user = User.objects.create_user(username=username, password=password)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class TrackersViewSet(viewsets.ModelViewSet):
    serializer_class = TrackerSerializer
    queryset = Tracker.objects.all()

class TrackerViewSet(viewsets.ModelViewSet):
    serializer_class = TrackerSerializer
    queryset = Tracker.objects.all()

    def list(self, request, code):
        tracker = Tracker.objects.filter(code=code).values_list('id')
        for item in tracker:
            id = item[0]
        product = Product.objects.filter(code=id)
        serializer_class = ProductSerializer(product, many=True)
        return Response(serializer_class.data)

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

