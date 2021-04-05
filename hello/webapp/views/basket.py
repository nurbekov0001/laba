from django.urls import reverse
from webapp.models import Product, Basket
from django.views.generic import ListView, DeleteView, View
from webapp.forms import ProductForm, SearchForm
from django.shortcuts import get_object_or_404, redirect, render


class BasketIndexView(ListView):
    template_name = 'basket/index.html'
    model = Basket
    context_object_name = 'baskets'




class BasketCreateView(View):

    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        product = Product.objects.get(pk=pk)
        if product.remainder > 0:
            try:
                basket = Basket.objects.get(product__pk=pk)
                product.remainder -= 1
                basket.amount += 1
                product.save()
                basket.save()
            except Basket.DoesNotExist:
                Basket.objects.create(product=product, amount=1)
                product.remainder -= 1
                product.save()

        else:
            pass
        return redirect('product_list')


class BasketDeleteView(DeleteView):
    model = Basket
    template_name = 'basket/delete.html'
    context_object_name = 'basket'


    def get_success_url(self):
        product = Product.objects.get(pk=self.object.product.pk)
        product.remainder += self.object.amount
        product.save()
        return reverse('basket_list')
