from django.shortcuts import render
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from .models import Chat, Transaction, Product, ProductImage, Category, User


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


@login_required()
def index(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    return HttpResponse("hi")


@csrf_exempt
def createProduct(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)


def retrieveProducts(request):
    user = User.objects.get(id=request.user.id)
    products = Product.objects.filter(
        user=user
    )
    products = products.order_by("-timestamp").all()
    return JsonResponse([product.serialize() for product in products], safe=False, status=201)

def retrieveOneProduct(request, product_id):
    product = Product.objects.filter(
        id=product_id
    )
    return JsonResponse(product.serialize(), safe=False)

@csrf_exempt
def createComment(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)


def retrieveComments(request):
    buyer = User.objects.get(id=request.user)
    comments = Chat.objects.filter(
        receiver=request.user, sender=buyer
    )
    comments = comments.order_by("-timestamp").all()
    return JsonResponse([comment.serialize() for comment in comments], safe=False)


@csrf_exempt
def createTransaction(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)

    seller = request.user
    buyer_id = data['buyer']
    product_id = data['product']
    product = Product.object.get(id=product_id)
    price = product.price
    cashback = product.cashback

    ## get the buyer id from the API request.
    try:
        buyer = User.object.get(id=buyer_id)
    except User.DoesNotExist:
        return JsonResponse({
            "error": f"User with id {buyer} does not exist."
        }, status=400)

    # create the transaction in the db and update the status of the product
    transaction = Transaction(
        product=product,
        seller=seller,
        buyer=buyer,
        price=price,
        cashback=cashback
    )
    transaction.save()

    product = product(active=False)
    product.save()

    return JsonResponse({"message": "A transação foi concluída com sucesso"}, status=201)


def retrieveTransactions(request):
    buyer = User.objects.get(id=request.user)
    transactions = Transaction.objects.filter(
        receiver=request.user, sender=buyer
    )
    transactions = transactions.order_by("-timestamp").all()
    return JsonResponse([transaction.serialize() for transaction in transactions], safe=False, status=201)