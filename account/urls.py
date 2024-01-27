from django.urls import path
from .views import (
    Register,
    Login,
    ForgotPassword,
    ResetPassword
)

urlpatterns = [
    path('register/',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('forgot/',ForgotPassword.as_view(),name='forgot'),
    path('reset/',ResetPassword.as_view(),name='reset'),
]