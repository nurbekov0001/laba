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
    BasketUpdateView,
    BasketView

)

urlpatterns = [
    path('', IndexView.as_view(), name='product_list'),
    path('<int:pk>/', ProductView.as_view(), name='product_view'),
    path('add/', ProductCreateView.as_view(), name='product_add'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('', BasketIndexView.as_view(), name='basket_list'),
    path('<int:pk>/', BasketView.as_view(), name='basket_view'),
    path('add/', BasketCreateView.as_view(), name='basket_add'),
    path('<int:pk>/update/', BasketUpdateView.as_view(), name='basket_update'),
    path('<int:pk>/delete/', BasketDeleteView.as_view(), name='basket_delete'),

]