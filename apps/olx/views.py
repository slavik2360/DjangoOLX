# Python
from typing import Any

# Django
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import (
    HttpResponse,
    JsonResponse
)
from django.views.generic import View
from django.db.models.query import QuerySet
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.contrib import messages
from django.views import View
# Create your views here.

#Local
from .models import (
    Product,
    Order
)
from .forms import (
    ProductForm,
    OrderForm
)

#Страница заказов
class IndexView(View):
    template_name='main/index.html'

    def get(self, request: WSGIRequest) -> HttpResponse:
        
        product = Product.objects.all()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'product' : product
            }
        )
    
#Создание продукта
class CreateProductView(View):
    template_name = 'main/create_product.html'

    def get(self, request: WSGIRequest):
        form = ProductForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
            }
        )

    def post(self, request: WSGIRequest):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
            }
        )
    
# Удаление продукта
class DeleteProductView(View):
    def get(self, request: WSGIRequest, product_id: int):
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('index')
    

#Страница заказов
class ListOrdersView(View):
    template_name = 'main/list_orders.html'

    def get(self, request: WSGIRequest):
        orders = Order.objects.all()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'orders': orders
            }
        )
    
    
# Создание Заказа
class CreateOrderView(View):
    template_name = 'main/create_order.html'

    def get(self, request: WSGIRequest):
        form = OrderForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
            }
        )

    def post(self, request: WSGIRequest):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_orders')
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
            }
        )

#Удаление заказов
class DeleteOrderView(View):
    def get(self, request: WSGIRequest, order_id: int):
        order = get_object_or_404(Order, id=order_id)
        order.delete()
        messages.success(request, 'Order deleted successfully.')
        return redirect('list_orders')

