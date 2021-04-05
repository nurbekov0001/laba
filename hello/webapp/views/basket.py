from django.urls import reverse
from webapp.models import Product, Basket, Order, IntermediateTable
from django.views.generic import ListView, DeleteView, View
from webapp.forms import  OrderForm
from django.shortcuts import  redirect
from django.utils.http import urlencode


class BasketIndexView(ListView):
    template_name = 'basket/index.html'
    model = Basket
    context_object_name = 'baskets'

    def get_sum_basket(self, **kwargs):
        sum = 0
        for product in Basket.objects.all():
            sum += product.amount * product.product.price
        return sum

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sum'] = self.get_sum_basket()
        context['form'] = OrderForm()
        return context


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


class OrderCreateView(View):


    def post(self, request, *args, **kwargs):
        form = OrderForm(data=request.POST)
        if form.is_valid():
            self.product_order = form.save()
            self.order()
            return redirect('product_list')
        return redirect('basket_list')

    def order(self):
        for order in Basket.objects.all():
            IntermediateTable.objects.create(product=order.product, order=self.product_order, amount=order.amount)
        Basket.objects.all().delete()
