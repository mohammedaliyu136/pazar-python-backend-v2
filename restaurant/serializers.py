from rest_framework import serializers

from .models import Banner, Restaurant, Product, Variation, AddOns, ChoiceOption, Category, Option, WishList

from django.contrib.auth.models import User
  
class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  '__all__'

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class VariationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variation
        fields = '__all__'

class AddOnsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddOns
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class OptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class ChoiceOptionSerializer(serializers.HyperlinkedModelSerializer):
    options = OptionSerializer(many=True,)
    class Meta:
        model = ChoiceOption
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    variations = VariationSerializer(many=True,)
    addons = AddOnsSerializer(many=True,)
    choice_options = ChoiceOptionSerializer(many=True,)
    category = CategorySerializer(many=True,)
    restaurant = RestaurantSerializer()
    class Meta:
        model = Product
        fields = '__all__'

class BannerSerializer(serializers.HyperlinkedModelSerializer):
    restaurant = RestaurantSerializer()
    class Meta:
        model = Banner
        fields = '__all__'

class WishListSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(many=True,)
    class Meta:
        model = WishList
        fields = '__all__'