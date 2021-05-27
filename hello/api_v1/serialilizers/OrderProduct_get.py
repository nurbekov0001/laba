from rest_framework import serializers

from webapp.models import IntermediateTable, Order


class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = IntermediateTable
        fields = ('product', 'amount', 'amount')


class OrderSerializer(serializers.ModelSerializer):
    intermediate_order = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'user_name', 'phone_number', 'address',  'created_at', 'intermediate_order')
        read_only_fields = ('id', 'created_at')
