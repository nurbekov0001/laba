from django.urls import path
from webapp.views import (
    IndexView,
    ProductView,
    ProductUpdateView,
    ProductDeleteView,
    ProductCreateView,
    # index_view,
    # product_view,
    # product_create_view,
    # product_update_view,
    # product_delete_view
)

urlpatterns = [
    path('', IndexView.as_view(), name='product_list'),
    path('<int:pk>/', ProductView.as_view(), name='product_view'),
    path('add/', ProductCreateView.as_view(), name='product_add'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

]