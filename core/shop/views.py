from django.views.generic.base import TemplateView


class ProductListView(TemplateView):
    template_name = "shop/product-list.html"


class SingleProductView(TemplateView):
    template_name = "shop/single-product.html"


class CartView(TemplateView):
    template_name = "shop/cart.html"


class CheckoutView(TemplateView):
    template_name = "shop/checkout.html"


class ConfirmationView(TemplateView):
    template_name = "shop/confirmation.html"
