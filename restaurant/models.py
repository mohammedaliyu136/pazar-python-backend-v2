#from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

class Restaurant(models.Model):
    image_url = models.CharField(max_length=300)
    name = models.CharField(max_length=30)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.CharField(max_length=40)
    min_order = models.FloatField()
    deliveryCharge = models.FloatField()

    def __str__(self):
        return self.name

class Variation(models.Model):
    type = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return self.type

class AddOns(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Option(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class ChoiceOption(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    options = models.ManyToManyField(Option)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=300)
    price = models.FloatField()
    variations = models.ManyToManyField(Variation)
    addons = models.ManyToManyField(AddOns)
    tax = models.FloatField()
    available_time_starts = models.TimeField()
    available_time_ends = models.TimeField()
    status = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attributes = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    choice_options = models.ManyToManyField(ChoiceOption)
    discount = models.FloatField()
    discount_type = models.CharField(max_length=30)
    tax_type = models.CharField(max_length=30)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.FloatField()

    def __str__(self):
        return self.name

class Banner(models.Model):
    name = models.CharField(max_length=30)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductWishList(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_id

class RestaurantWishList(models.Model):
    user_id = models.IntegerField()
    restaurant_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.restaurant_id
        
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    products = models.ManyToManyField(Product)

    coupon_discount_amount = models.FloatField()
    coupon_discount_title = models.CharField(max_length=100)
    order_amount = models.FloatField()
    order_type = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=100)
    contact_person_name = models.CharField(max_length=100)
    contact_person_phone = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=1000)
    order_note = models.CharField(max_length=200, blank=True)
    coupon_code = models.CharField(max_length=100)
    order_status = models.CharField(max_length=100, default='pending')



    def __str__(self):
        return self.user.first_name+ ' ' + self.user.last_name

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=30, default='pending')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    discount_on_product = models.FloatField()
    quantity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

class PromoCode(models.Model):
    title = models.CharField(max_length=30,)
    code = models.CharField(max_length=30,)
    discount_type = models.CharField(max_length=30,)
    status = models.CharField(max_length=30,)
    code = models.CharField(max_length=30,)
    discount = models.FloatField()
    discount = models.FloatField()
    min_purchase = models.FloatField()
    max_discount = models.FloatField()

    start_date = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField(auto_now=True)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code+' - '+self.title
