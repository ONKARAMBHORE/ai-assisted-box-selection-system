from rest_framework import serializers

from .models import Order, OrderItem

# serializer for the order items
class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id","product","product_name","quantity",]
        read_only_fields = ["id","product_name"]

# order serializers

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id","items","created_at",]
        read_only_fields = ["id", "created_At"]


# create order first an than creates its orderItems
    def create(self, validated_data):
        items_data = validated_data.pop("items")

        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order