from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("user", "price", "cashback", "description", "active", "timestamp", "image")
