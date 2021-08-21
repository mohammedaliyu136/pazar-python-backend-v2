from account.models import Address
from rest_framework import viewsets
from .serializers import userSerializers, AddressSerializers, ProfileSerializers, ConfigSerializers
from django.contrib.auth.models import User
from .models import Address, Profile, ConfigModel

from rest_framework.permissions import AllowAny, IsAuthenticated
  
  
class Userviewsets(viewsets.ModelViewSet):
    #permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = userSerializers  

class Addressviewsets(viewsets.ModelViewSet):
    #permission_classes = [AllowAny]
    queryset = Address.objects.all()
    serializer_class = AddressSerializers  

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        if(user.id != None):
            return Address.objects.filter(user_id=user.id)
        else:
            queryset = Address.objects.all()

class Profileviewsets(viewsets.ModelViewSet):
    #permission_classes = [AllowAny]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers

class Configviewsets(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = ConfigModel.objects.all()
    serializer_class = ConfigSerializers