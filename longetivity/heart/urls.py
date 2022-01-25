from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('form/', views.form, name = 'form'),
    path('database/', views.database, name = 'database'),
    path('result/', views.result, name = 'result'),
    path('editbase/<str:pk>/', views.editbase, name = 'editbase'),
    path('deletebase/<str:pk>/', views.deletebase, name = 'deletebase'),
    path('multi/<str:pk>/', views.multi, name = 'multi'),
]