from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from api_v1.serialilizers.OrderProduct import OrderSerializer
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from api_v1.serialilizers.product import ProductSerializer
from webapp.models import Order, Product


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class LogoutView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # def get_permissions(self):
    #    if self.request.method in SAFE_METHODS:
    #       return []
    #    return super().get_permissions()
