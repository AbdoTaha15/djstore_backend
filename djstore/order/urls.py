from django.urls import path
from order.views import OrderList
from order import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrderList.as_view()),
]