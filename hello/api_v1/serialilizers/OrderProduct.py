from rest_framework import serializers

from webapp.models import IntermediateTable, Order


class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = IntermediateTable
        fields = ('product', 'amount')


class OrderSerializer(serializers.ModelSerializer):
    intermediate_order = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('user', 'user_name', 'phone_number', 'address',  'intermediate_order')
        read_only_fields = ('id', 'created_at')

    def create(self, validated_data):
        print(validated_data)
        order_product = validated_data.pop('intermediate_order')
        order = Order.objects.create(**validated_data)
        for i in order_product:
            a = IntermediateTable(
                product=i['product'], order=order, amount=i['amount'])
            a.save()
        validated_data['intermediate_order'] = order_product
        return validated_data

