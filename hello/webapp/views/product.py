from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from webapp.models import Product
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from webapp.forms import ProductForm, SearchForm

from django.db.models import Q
from django.utils.http import urlencode


class IndexView(ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(IndexView, self).get(request, **kwargs)

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


class ProductView(DetailView):
    model = Product
    template_name = 'product/view.html'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'product/create.html'
    model = Product
    form_class = ProductForm
    permission_required = "webapp.add_product"


    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/update.html'
    form_class = ProductForm
    context_object_name = 'product'
    permission_required = "webapp.change_product"

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin,DeleteView):
    model = Product
    template_name = 'product/delete.html'
    context_object_name = 'product'
    permission_required = "webapp.delete_product"

    def get_success_url(self):
        return reverse('product_list')
