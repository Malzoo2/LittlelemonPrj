from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MenuItem, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"

class BookSerializer (serializers.ModelSerializer):
    class Meta:
        model: Booking
        fields = "__all__"
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']
