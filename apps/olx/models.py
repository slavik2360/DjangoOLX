from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):

    name = models.CharField(
        verbose_name='наименование',
        max_length=120
    )
    description = models.CharField(
        verbose_name='описание',
        max_length=500
    )
    image = models.URLField(
        verbose_name='ссылка на изображение',
    )
    price = models.DecimalField(
        verbose_name='цена',
        decimal_places=2,
        max_digits=12
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self) -> str:
        return f'{self.name} <:> {self.price}'


class Order(models.Model):

    user = models.ForeignKey(
        verbose_name='юзер',
        to=User, 
        on_delete=models.CASCADE,
        related_name='order')
    product = models.ForeignKey(
        verbose_name='продукт',
        to=Product, 
        on_delete=models.CASCADE,
        related_name='item'
    )
    money = models.DecimalField(
        verbose_name='общая стоимость',
        decimal_places=2,
        max_digits=12
    )
    
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self) -> str:
        return f'{self.user} <:> {self.product}'