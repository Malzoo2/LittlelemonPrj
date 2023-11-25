from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

