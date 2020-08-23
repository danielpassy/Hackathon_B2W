from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    # authenticate
    path('api-token-auth', obtain_auth_token, name='api_token_auth'),
    # path("logout", views.logout_view, name="logout"),
    # path("register", views.register, name="register"),

    # API Routes
    path("login", views.login_view, name="login"),
    path("products", views.createProduct, name="createProduct"),
    path("products/<str:id>", views.retrieveOneProduct, name="retrieveOneProduct"),
    path("products/user/<str:id>", views.retrieveUserProducts, name="retrieveProducts"),
    path("comments", views.createComment, name="createComment"),
    path("comments/user", views.retrieveComments, name="retrieveComments"),
    path("transaction", views.createTransaction, name="createTransaction"),
    path("transaction/list/<str:id>", views.retrieveTransactions, name="retrieveTransactions")
]




