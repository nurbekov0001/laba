from django.http import request
from django.urls import reverse
from webapp.models import Product, Basket, Order, IntermediateTable
from django.views.generic import ListView, DeleteView, View
from webapp.forms import OrderForm
from django.shortcuts import redirect


class BasketIndexView(ListView):
    template_name = 'basket/index.html'
    model = Basket
    context_object_name = 'baskets'


    def get_queryset(self):
        session = self.request.session.get('basket', [])
        return Basket.objects.filter(pk__in=session)

    def get_sum_basket(self, **kwargs):
        sum = 0
        for product in self.get_queryset():
            sum += product.amount * product.product.price
        return sum


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sum'] = self.get_sum_basket()
        context['form'] = OrderForm()
        return context


class BasketCreateView(View):

    def get(self, request, *args, **kwargs):
        session = request.session.get('basket', [])
        pk = kwargs.get("pk")
        product = Product.objects.get(pk=pk)
        if product.remainder > 0:
            try:
                basket = Basket.objects.get(product__pk=pk, pk__in=session)
                basket.amount += 1
                basket.save()
            except Basket.DoesNotExist:
                basket = Basket.objects.create(product=product, amount=1)
                session.append(basket.pk)
                request.session['basket'] = session
        return redirect('product_list')


class BasketDeleteView(DeleteView):
    model = Basket
    template_name = 'basket/delete.html'
    context_object_name = 'basket'

    def get(self, request, *args, **kwargs):
        session = request.session.get('basket', [])
        print(session)
        basket = Basket.objects.get(pk=self.get_object().pk)
        session.remove(basket.pk)
        request.session['basket'] = session
        return super().delete(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
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
        session = self.request.session.get('basket', [])
        for order in Basket.objects.filter(pk__in=session):
            product = order.product
            if product.remainder >= order.amount:
                IntermediateTable.objects.create(product=order.product, order=self.product_order, amount=order.amount)
                product.remainder -= order.amount
                product.save()
            order.delete()



class ViewOrders(ListView):
    model = IntermediateTable
    template_name = "basket/orders.html"
    context_object_name = 'order'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
