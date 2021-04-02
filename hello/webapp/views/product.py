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


class ProductCreateView(CreateView):
    template_name = 'product/create.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


#
# class ProjectTracerCreate(CreateView):
#     model = Tracer
#     template_name = 'tracer/create.html'
#     form_class = TracerForm
#
#     def form_valid(self, form):
#         project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
#         tracer = form.save(commit=False)
#         tracer.project = project
#         tracer.save()
#         form.save_m2m()
#         return redirect('project_view', pk=project.pk)
#


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/update.html'
    form_class = ProductForm
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete.html'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})
