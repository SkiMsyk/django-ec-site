from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Pay
    path('pay/checkout/', views.PayWithStripe.as_view()),
    path('pay/success/', views.PaySuccessView.as_view()),
    path('pay/cancel/', views.PayCancelView.as_view()),
    
    # Items
    path('items/<str:pk>/', views.ItemDetailView.as_view()),
    
    # Cart
    path('cart/', views.CartListView.as_view()),
    path('cart/add/', views.AddCartView.as_view()),
    path('cart/remove/<str:pk>/', views.remove_from_cart),
    
    # index
    path('', views.IndexListView.as_view()),
]
