
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Address, Profile, ConfigModel
  
class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  '__all__'

class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields =  '__all__'


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =  '__all__'       

class ConfigSerializers(serializers.ModelSerializer):
    class Meta:
        model = ConfigModel
        fields =  '__all__'
