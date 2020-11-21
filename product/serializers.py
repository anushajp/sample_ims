
from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'quantity', 'price',
            'created_on', 'updated_on',
        )

    def create(self, validated_data):
        """
        Create and return a new Product instance.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update the product instance
        """
        instance.name = validated_data.get('name', instance.name)
        instance.quantity = validated_data.get('quantity', instance.code)
        instance.price = validated_data.get('price', instance.linenos)
        instance.description = validated_data.get('description', instance.language)
        instance.save()
        return instance
