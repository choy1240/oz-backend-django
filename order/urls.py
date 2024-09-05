from django.urls import path
from .views import OrderCreateView, OrderUpdateView, OrderDeleteView, OrderDetailView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),
    path('<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]
