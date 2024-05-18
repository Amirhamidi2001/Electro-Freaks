from django.urls import path

from accounts.views import LoginView, SignupView

app_name = "accounts"

urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
]
