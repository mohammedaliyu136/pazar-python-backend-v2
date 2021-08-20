#from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.fields import CharField

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

class WishList(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name
