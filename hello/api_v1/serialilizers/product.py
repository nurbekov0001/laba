from rest_framework import serializers

from webapp.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category', 'remainder', 'price')
        read_only_fields = ('id',)

