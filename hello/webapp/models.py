from django.db import models
from django.core.validators import MinValueValidator

CATEGORY_CHOICES = [('OTHER', 'other'), ('SAMSUNG', 'samsung'), ('ACER', 'acer'), ('IPHONE', 'iPhone')]





class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Наименование товара")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание товара")
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, null=False, blank=False, default='other',
                                verbose_name="категория товара")
    remainder = models.IntegerField(null=False, blank=False,  validators=[MinValueValidator(0)], verbose_name="Остаток")
    price = models.DecimalField(null=False, blank=False, validators=[MinValueValidator(0)], max_digits=7,
                                decimal_places=2, verbose_name="Стоимость")

    class Meta:
        db_table = 'Products'
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f'{self.id}. {self.name}:{self.description} {self.category} {self.remainder}{self.price}'


class Basket(models.Model):
    product = models.ForeignKey("webapp.Product", related_name='product', on_delete=models.CASCADE,
                                verbose_name="Наименование продукта",)
    amount = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Количество")

    def __str__(self):
        return f'{self.product.name},{self.amount}'

# Create your models here.


