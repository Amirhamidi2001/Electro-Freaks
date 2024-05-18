from django.urls import path

from shop.views import ProductListView, SingleProductView, CartView, CheckoutView, ConfirmationView

app_name = "shop"

urlpatterns = [
    path("", ProductListView.as_view(), name="shop"),
    path("product/", SingleProductView.as_view(), name="product"),
    path("cart/", CartView.as_view(), name="cart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("confirmation/", ConfirmationView.as_view(), name="confirmation"),
]
