from rest_framework import serializers

from .models import Banner, ProductWishList, RestaurantWishList, Restaurant, Product, Variation, AddOns, ChoiceOption, Category, Option

from django.contrib.auth.models import User
  
class userSerializers(serializers.ModelSerializer):
    #id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields =  '__all__'

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    #id = serializers.ReadOnlyField()
    class Meta:
        model = Restaurant
        fields = '__all__'

class VariationSerializer(serializers.HyperlinkedModelSerializer):
    #id = serializers.ReadOnlyField()
    class Meta:
        model = Variation
        fields = '__all__'

class AddOnsSerializer(serializers.HyperlinkedModelSerializer):
    #id = serializers.ReadOnlyField()
    class Meta:
        model = AddOns
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    #id = serializers.ReadOnlyField()
    class Meta:
        model = Category
        fields = '__all__'

class OptionSerializer(serializers.HyperlinkedModelSerializer):
    #id = serializers.ReadOnlyField()
    class Meta:
        model = Option
        fields = '__all__'

class ChoiceOptionSerializer(serializers.HyperlinkedModelSerializer):
    #id = serializers.ReadOnlyField()
    #options = OptionSerializer(many=True,)
    class Meta:
        model = ChoiceOption
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    #id = serializers.ReadOnlyField()
    #variations = VariationSerializer(many=True,)
    #addons = AddOnsSerializer(many=True,)
    #choice_options = ChoiceOptionSerializer(many=True,)
    #category = CategorySerializer(many=True,)
    #restaurant = RestaurantSerializer()
    class Meta:
        model = Product
        fields = '__all__'

class BannerSerializer(serializers.HyperlinkedModelSerializer):
    #id = serializers.ReadOnlyField()
    #restaurant = RestaurantSerializer()
    class Meta:
        model = Banner
        fields = '__all__'

class ProductWishListSerializer(serializers.HyperlinkedModelSerializer):
    #id = serializers.ReadOnlyField()
    #product = ProductSerializer()
    #user = userSerializers()
    class Meta:
        model = ProductWishList
        fields = '__all__'

class RestaurantWishListSerializer(serializers.HyperlinkedModelSerializer):
    #id = serializers.ReadOnlyField()
    #restaurant = RestaurantSerializer()
    class Meta:
        model = RestaurantWishList
        fields = '__all__'