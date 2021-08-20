from django.shortcuts import render
from django.http import HttpResponse, response
import datetime

from rest_framework.authtoken.models import Token

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import AllowAny

from rest_framework.authtoken.models import Token
from django.http import JsonResponse

from rest_framework import status

from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView

from .serializers import BannerSerializer, RestaurantSerializer, ProductSerializer, VariationSerializer, AddOnsSerializer, ChoiceOptionSerializer, CategorySerializer, OptionSerializer, WishListSerializer, userSerializers
from .models import Banner, Category, Restaurant, Product, Variation, AddOns, ChoiceOption, Category, Option, Profile, WishList
from django.contrib.auth.models import User


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all().order_by('name')
    serializer_class = RestaurantSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

class VariationViewSet(viewsets.ModelViewSet):
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer

class AddOnsViewSet(viewsets.ModelViewSet):
    queryset = AddOns.objects.all()
    serializer_class = AddOnsSerializer

class ChoiceOptionViewSet(viewsets.ModelViewSet):
    queryset = ChoiceOption.objects.all()
    serializer_class = ChoiceOptionSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer

class ArticleListCreateAPIView(APIView):
    def get(self, request):
        return response({})


@api_view(["GET"])
@permission_classes((AllowAny, ))
def user_info(request):
    if(request.user.is_anonymous == False):
        return JsonResponse(userSerializers(request.user).data,)
    else:
        json = {
            'message':'Please Sign in',
            }
        return Response(json, status=status.HTTP_401_UNAUTHORIZED)

@csrf_exempt
def user_login(request):
    now = datetime.datetime.now()
    if(request.method=='POST'):
        try:
            profile = Profile.objects.get(email=request.POST.get('email'))
            if(profile.password != request.POST.get('password')):
                json = {
                    'message':'Invalid credential',
                    'status':404
                    }
                return JsonResponse(json)

        except Profile.DoesNotExist:
            profile = None
        
        if(profile is not None):
            json = {
                'pk':str(profile.pk),
                'name':profile.name,
                'phone':profile.phone,
                'email':profile.email,
                'token':'d5d86e55fd5ddd48298b2ac72c3ed96b7e30dd86'
                }
            return JsonResponse(json)
        json = {'message':'Invalid credential','status':404}
        return JsonResponse(json)
    
    html = "<html><body>Invalid credential</br> %s.</body></html>" % now
    return HttpResponse(html)

@csrf_exempt
@api_view(["POST"])
def user_register(request):
    now = datetime.datetime.now()
    print(request)
    if(request.method=='POST'):
        try:
            print(request.POST)
            user = User(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            username=request.POST.get('username'),
            )
            user.set_password(request.POST.get('password'))
            user.save()
            #profile = Profile(name=request.POST.get('name'), phone=request.POST.get('phone'), email=request.POST.get('email'), password=request.POST.get('password'))
            #profile.save()
            token = Token.objects.create(user=user)
            json = {
                'token':token.key
            }
            #return Response(json, status=status.HTTP_201_CREATED)
            return JsonResponse(json)
        except:
            json = {
                'message': 'Error while creating your account',
            }
            #return Response(json, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse(json)
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

@csrf_exempt
@api_view(["POST"])
def user_registerrr(request):
    now = datetime.datetime.now()
    print(request)
    if(request.method=='POST'):
        try:
            print(request.POST)
            
            json = {
                'token':"token.key"
            }
            #return Response(json, status=status.HTTP_201_CREATED)
            return JsonResponse(json)
        except:
            json = {
                'message': 'Error while creating your account',
            }
            #return Response(json, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse(json)
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
