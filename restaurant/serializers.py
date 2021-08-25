from rest_framework import serializers

from .models import Banner, Order, OrderDetail, ProductWishList, RestaurantWishList, Restaurant, Product, Variation, AddOns, ChoiceOption, Category, Option

from django.contrib.auth.models import User
  
class userSerializers(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields =  '__all__'

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Restaurant
        fields = '__all__'

class VariationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Variation
        fields = '__all__'

class AddOnsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = AddOns
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Category
        fields = '__all__'

class OptionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Option
        fields = '__all__'

class ChoiceOptionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    options = OptionSerializer(many=True,)
    class Meta:
        model = ChoiceOption
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    variations = VariationSerializer(many=True,)
    addons = AddOnsSerializer(many=True,)
    choice_options = ChoiceOptionSerializer(many=True,)
    category = CategorySerializer(many=True,)
    restaurant = RestaurantSerializer()
    class Meta:
        model = Product
        fields = '__all__'

class BannerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    restaurant = RestaurantSerializer()
    class Meta:
        model = Banner
        fields = '__all__'

class ProductWishListSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    product = ProductSerializer()
    user = userSerializers()
    class Meta:
        model = ProductWishList
        fields = '__all__'

class RestaurantWishListSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    restaurant = RestaurantSerializer()
    class Meta:
        model = RestaurantWishList
        fields = '__all__'

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Order
        fields = '__all__'

class RegisterationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}
    
    def save(self):
        print('0000000000000000000')
        print(self.validated_data['email'])
        account = User(
            username=self.validated_data['username'],
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        account.set_password(password)
        account.save()

class PlaceOrderSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    restaurant_id = serializers.CharField()
    order_amount = serializers.CharField()
    coupon_discount_amount = serializers.CharField()
    coupon_discount_title = serializers.CharField()
    payment_status = serializers.CharField()
    order_status = serializers.CharField()
    payment_method = serializers.CharField()
    transaction_reference = serializers.CharField()
    delivery_address_id = serializers.CharField()
    delivery_charge = serializers.CharField()
    order_note = serializers.CharField(allow_blank=True)
    details_count = serializers.CharField()
    addon_id = serializers.CharField()
    order_type = serializers.CharField()


class OrderDetailSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    order = OrderSerializer()
    product = ProductSerializer()
    class Meta:
        model = OrderDetail
        fields = '__all__'


class AddProductWishListSerializer(serializers.Serializer):
    # _user_id, order_amount, coupon_discount_amount, coupon_discount_title, payment_status, order_status, payment_method, 
    #       transaction_reference, delivery_address_id, delivery_man_id, delivery_charge, order_note, details_count, addons
    product_id = serializers.CharField()
    user_id = serializers.CharField()
    