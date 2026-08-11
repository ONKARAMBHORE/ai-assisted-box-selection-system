from django.shortcuts import render
from .models import Box
from rest_framework import viewsets
from .serializers import BoxSerializer

# crud operations for the Box

class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all().order_by("cost")
    serializer_class = BoxSerializer