from django.urls import path
from webapp.views import (
    index_view,
    product_view,
    product_create_view,
    product_update_view,
    product_delete_view
)

urlpatterns = [
    path('', index_view, name='product_list'),
    path('<int:pk>/', product_view, name='product_view'),
    path('add/', product_create_view, name='product_add'),
    path('<int:pk>/update/', product_update_view, name='product_update'),
    path('<int:pk>/delete/', product_delete_view, name='product_delete'),

]