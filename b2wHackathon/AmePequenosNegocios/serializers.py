from rest_framework import serializers
from .models import *


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "products"]

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"
        read_only_fields = ("timestamp", )

class ProductSerializer(serializers.ModelSerializer):
    categorias = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )

    class Meta:
        model = Product
        fields = ("categorias", "name", "user", "price", "cashback", "description", "active", "timestamp", "image")
        read_only_fields = ("active", "timestamp",)

class TransactionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ("__all__")
        read_only_fields = ("timestamp",)