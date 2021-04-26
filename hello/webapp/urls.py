from django.urls import path
from webapp.views import (
    IndexView,
    ProductView,
    ProductUpdateView,
    ProductDeleteView,
    ProductCreateView,
    BasketIndexView,
    BasketCreateView,
    BasketDeleteView,
    OrderCreateView
)


urlpatterns = [
    path('', IndexView.as_view(), name='product_list'),
    path('<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),


    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('basket/', BasketIndexView.as_view(), name='basket_list'),
    path('add/<int:pk>', BasketCreateView.as_view(), name='basket_add'),
    path('delete/<int:pk>', BasketDeleteView.as_view(), name='basket_delete'),
    path('add/', OrderCreateView.as_view(), name='order_add'),


]