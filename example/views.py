from django.shortcuts import render
from rest_framework import generics
from .models import Stuff
from .serializers import StuffSerializer

# Create your views here.
def index(request):
    return render(reuest, 'example/index.html', {})

class StuffList(generics.ListCreateAPIView):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer

class StuffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer
