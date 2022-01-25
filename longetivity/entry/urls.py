from django.urls import path, URLPattern
from . import views

urlpatterns = [
    path('loginpage/', views.loginpage, name = 'loginpage'),
    path('signup/', views.signup, name = 'signup' ),
    path('signin/', views.signin, name = 'signin'),
    path('signout/', views.signout, name = 'signout'),
]