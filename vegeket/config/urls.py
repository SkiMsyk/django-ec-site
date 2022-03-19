from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Items
    path('items/<str:pk>/', views.ItemDetailView.as_view()),
    
    # Cart
    path('cart/', views.CartListView.as_view()),
    path('cart/add', views.AddCartView.as_view()),
    
    # index
    path('', views.IndexListView.as_view()),
]
