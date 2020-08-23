import json
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
import operator


@api_view(['POST', 'GET'])
@csrf_exempt
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "AmePequenosNegocios/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "AmePequenosNegocios/login.html")


def index(request):
    return HttpResponse("hi")


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
@csrf_exempt
@permission_classes([IsAuthenticated])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        saved_product = serializer.save()
        serializer_category = CategorySerializer(data=request.data)
        if serializer_category.is_valid():
            serializer_category.validated_data['products'] = saved_product
            saved_category = serializer_category.save()
        else:
            print("deu ruim fodaci")
            # product = Product.objects.get(id=saved_product.id)
            # DB_entry = Category.objects.create(name=category, products=product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
@permission_classes([AllowAny])
def retrieveUserProducts(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    products = Product.objects.filter(
        user=user
    )
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def retrieveOneProduct(request, id):
    product = Product.objects.filter(
        id=id
    )
    serializer = ProductSerializer(product, context={'request': request}, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def createComment(request):
    serializer = ChatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@parser_classes([MultiPartParser, FormParser])
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def retrieveComments(request):
    try:
        data = json.loads(request.body)
        seller = data['seller']
        buyer = data['buyer']
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    chat = Chat.objects.filter(
        seller=seller, buyer=buyer
    )
    chat = chat.order_by("-timestamp").all()
    serializer = ChatSerializer(chat, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def createTransaction(request):
    try:
        data = json.loads(request.body)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = TransactionsSerializer(data=data)
    try:
        product_id = data['product']
        owner = data['seller']
    except:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    product = Product.objects.get(id=product_id)
    if (product.active == True and product.user.id == owner):
        if serializer.is_valid():
            serializer.save()
            product.active = False
            product.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response("The seller it's not the owner of the productq", status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def retrieveTransactions(request, id):
    try:
        seller = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    transactions = Transaction.objects.filter(
        Q(seller=seller) | Q(buyer=seller)
    )
    transactions = transactions.order_by("-timestamp").all()
    serializer = TransactionsSerializer(transactions, many=True)
    return Response(serializer.data)