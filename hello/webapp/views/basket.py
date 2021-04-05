from django.urls import reverse
from webapp.models import Product
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from webapp.forms import ProductForm, SearchForm
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from django.utils.http import urlencode


class BasketIndexView(ListView):
    template_name = 'basket/index.html'
    model = Product
    context_object_name = 'basket'
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(BasketIndexView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(name__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        return queryset.order_by('name', 'category').exclude(remainder=0)

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context


class BasketView(DetailView):
    model = Product
    template_name = 'basket/view.html'


class BasketCreateView(CreateView):
    template_name = 'basket/create.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('basket_view', kwargs={'pk': self.object.pk})



# class BasketProductCreate(CreateView):
#     model = Product
#     template_name = 'product/create.html'
#     form_class = ProductForm
#
#     def form_valid(self, form):
#         project = get_object_or_404(Product, pk=self.kwargs.get('pk'))
#         tracer = form.save(commit=False)
#         tracer.project = project
#         tracer.save()
#         form.save_m2m()
#         return redirect('basket_view', pk=project.pk)
#


class BasketUpdateView(UpdateView):
    model = Product
    template_name = 'basket/update.html'
    form_class = ProductForm
    context_object_name = 'basket'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class BasketDeleteView(DeleteView):
    model = Product
    template_name = 'basket/delete.html'
    context_object_name = 'basket'

    def get_success_url(self):
        return reverse('basket_view', kwargs={'pk': self.object.pk})
