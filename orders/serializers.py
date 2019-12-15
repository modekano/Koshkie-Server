from rest_framework import serializers

from accounts.serializers import UserProfileSerializer, UserAddressSerializer
from drivers.serializers import DriverProfileSerializer
from orders.models import OrderModel, OrderItemModel, Choice
from shops.serializers import ShopProfileSerializer


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('option_group', 'choosed_option')


class OrderItemSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = OrderItemModel
        fields = ('product', 'quantity', 'choices', 'add_ons', 'special_request')
        extra_kwargs = {
            'special_request': {'required': False}
        }


class OrderSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(many=False, read_only=True)
    driver = DriverProfileSerializer(many=False, read_only=True)
    shops = ShopProfileSerializer(many=True, read_only=True)
    items = OrderItemSerializer(many=True)
    shipping_address = UserAddressSerializer(many=False)

    class Meta:
        model = OrderModel
        fields = ('user', 'driver', 'shops', 'items', 'ordered_at', 'shipping_address',
                  'arrived', 'final_price', 'delivery_fee', 'vat')
        read_only_fields = ('user', 'driver', 'shops', 'ordered_at',
                            'arrived', 'final_price', 'delivery_fee', 'vat')
