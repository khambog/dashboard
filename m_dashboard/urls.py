from django.urls import path
from .import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='Home'),
    path('product/', views.product, name='Product'),
    path('customer/<str:pk_test>/', views.customer, name='Customer'),
    path('create_order/', views.createOrder, name='Create_order'),
    path('update_order/<str:id>/', views.updateOrder, name='Update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name = 'Delete_order')


]
