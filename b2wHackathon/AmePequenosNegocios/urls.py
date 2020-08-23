from django.urls import path

from . import views

urlpatterns = [
    path("login", views.login_view, name="login"),
    # path("logout", views.logout_view, name="logout"),
    # path("register", views.register, name="register"),

    # API Routes
    path("products", views.createProduct, name="createProduct"),
    path("products/list", views.retrieveProducts, name="retrieveProducts"),
    path("products/list/<str:id>", views.retrieveOneProduct, name="retrieveOneProduct"),
    path("comments", views.createComment, name="createComment"),
    path("comments/list", views.retrieveComments, name="retrieveComments"),
    path("transaction", views.createTransaction, name="createTransaction"),
    path("transaction/list", views.retrieveTransactions, name="retrieveTransactions")
]
