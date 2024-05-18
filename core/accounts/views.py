from django.views.generic.base import TemplateView


class LoginView(TemplateView):
    template_name = "accounts/login.html"


class SignupView(TemplateView):
    template_name = "accounts/signup.html"
