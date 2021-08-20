from restaurant.models import Restaurant
from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    address_type = models.CharField(max_length=30)
    contact_person_name = models.CharField(max_length=30)
    contact_person_number = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    _method = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contact_person_name


class Profile(models.Model):
    phone = models.CharField(max_length=11)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone

class ConfigModel(models.Model):
    company_name = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=30)
    contact_email = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    digital_payment = models.BooleanField()
    cash_payment = models.BooleanField()
    digital_payment_key = models.CharField(max_length=100)

    terms_and_condition = models.CharField(max_length=200)
    privacy_policy = models.CharField(max_length=200)
    about_us = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
