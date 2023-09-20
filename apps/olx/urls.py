from django.urls import path
from .views import (
   IndexView,
   CreateProductView,
   DeleteProductView,
   CreateOrderView,
   ListOrdersView,
   DeleteOrderView,
)

urlpatterns = [
   path('', IndexView.as_view(), name='index'),
   path('create_product/', CreateProductView.as_view(), name='create_product'),
   path('delete_product/<int:product_id>/', DeleteProductView.as_view(), name='delete_product'),
   path('create_order/', CreateOrderView.as_view(), name='create_order'),
   path('list_orders/', ListOrdersView.as_view(), name='list_orders'),
   path('delete_order/<int:order_id>/', DeleteOrderView.as_view(), name='delete_order')
]
