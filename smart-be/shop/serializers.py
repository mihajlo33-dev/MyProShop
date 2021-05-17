from rest_framework import serializers
from .models import product, tshirt, shoes, sweatshirt, jeans, bag, shoes

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = product
        fields = ('name', 'price', 'description', 'image')


class TshirtSerializer(serializers.ModelSerializer):

    class Meta:
        model = tshirt
        fields = ('brand', 'model', 'gender', 'price', 'description', 'image')


class ShoesSerializer(serializers.ModelSerializer):

    class Meta:
        model = shoes
        fields = ('brand', 'model', 'gender', 'price', 'description', 'image')



class SweatshirtSerializer(serializers.ModelSerializer):

    class Meta:
        model = sweatshirt
        fields = ('brand', 'model', 'gender', 'price', 'description', 'image')


class JeansSerializer(serializers.ModelSerializer):

    class Meta:
        model = jeans
        fields = ('brand', 'model', 'gender', 'price', 'description', 'image')


class BagSerializer(serializers.ModelSerializer):

    class Meta:
        model = bag
        fields = ('brand', 'model', 'gender', 'price', 'description', 'image')