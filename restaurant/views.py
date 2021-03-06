from account.models import Address
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

from .serializers import AddProductWishListSerializer, BannerSerializer, OrderDetailSerializer, OrderSerializer, PlaceOrderSerializer, ProductWishListSerializer, PromoCodeSerializer, RegisterationSerializer, RestaurantSerializer, ProductSerializer, RestaurantWishListSerializer, VariationSerializer, AddOnsSerializer, ChoiceOptionSerializer, CategorySerializer, OptionSerializer, userSerializers
from .models import Banner, Category, Order, OrderDetail, ProductWishList, PromoCode, Restaurant, Product, RestaurantWishList, Variation, AddOns, ChoiceOption, Category, Option, Profile
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

class ProductWishListViewSet(viewsets.ModelViewSet):
    queryset = ProductWishList.objects.all()
    serializer_class = ProductWishListSerializer

    def get(self, request,):
        print('1111111111')
        print(self)

class RestaurantWishListViewSet(viewsets.ModelViewSet):
    queryset = RestaurantWishList.objects.all()
    serializer_class = RestaurantWishListSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

class PromoCodeViewSet(viewsets.ModelViewSet):
    queryset = PromoCode.objects.all()
    serializer_class = PromoCodeSerializer


class ArticleListCreateAPIView(APIView):
    def get(self, request):
        return response({})


@api_view(["GET"])
@permission_classes((AllowAny, ))
def apply_coupon(request):
    print(request.GET['code'])
    if(request.GET['code'] != None):
        try:
            promoCode = PromoCode.objects.get(code=request.GET['code'])
        except:
            return Response({},status=status.HTTP_404_NOT_FOUND)
        serializer_context = {'request': request}#Request(request),}

        s = PromoCodeSerializer(instance=promoCode, context=serializer_context)
        return Response(s.data, status=status.HTTP_200_OK)
    else:
        json = {
            'message':'Please Sign in',
            }
        return Response(json, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
@permission_classes((AllowAny, ))
def search(request):
    print(request.GET['name'])
    if(request.GET['name'] != None):
        try:
            products = Product.objects.filter(name__icontains=request.GET['name'])
        except:
            return Response({},status=status.HTTP_404_NOT_FOUND)
        serializer_context = {'request': request}#Request(request),}

        ProductSerialized = ProductSerializer(instance=products, many=True, context=serializer_context)
        return Response(ProductSerialized.data, status=status.HTTP_200_OK)
    else:
        json = {
            'message':'Please Sign in',
            }
        return Response(json, status=status.HTTP_404_NOT_FOUND)


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
#@api_view(["GET"])
def add_product_wish_list2(request):
    now = datetime.datetime.now()
    product = Product.objects.get(pk=request.GET.get('product'))
    user = User.objects.get(pk=request.GET.get('user'))
    print("product_id "+request.GET.get('product'))
    print("user_id "+request.GET.get('user'))
    print(product)
    print(user)
    product_wish_list_count = ProductWishList.objects.filter(
            product=product.pk, 
            user = user.pk)
    if(len(product_wish_list_count)==0):
            ProductWishList(product=product.pk, 
            user = user.pk).save()
        
        
    json = {'message':'Invalid credential','status':404}
    return JsonResponse(json)


@api_view(['POST'])
def add_product_wish_list(request):
    if request.method == 'POST':
        serializer = AddProductWishListSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = User.objects.get(pk=serializer.data['user_id'])
            product = Product.objects.get(pk=serializer.data['product_id'])
            print(user)
            print(product)
            product_wish_list_count = ProductWishList.objects.filter(
            product=product.pk, 
            user = user.pk)
            print(product_wish_list_count)
            if(len(product_wish_list_count)==0):
                ProductWishList(product=product, user = user).save()

            data['reponse'] = "Successfully registered a new user."
            #data['email'] = account.email
            #data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)

@api_view(['POST'])
def registeration_view(request):
    if request.method == 'POST':
        serializer = RegisterationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            print('poopopopopopooppo')
            print(serializer.data['username'])
            user = User.objects.get(username=serializer.data['username'])
            print(user)
            token = Token.objects.create(user=user)
            data['token'] = token.key
            print(token.key)

            data['reponse'] = "Successfully registered a new user."
            #data['email'] = account.email
            #data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)

@api_view(['POST'])
def place_order_view(request):
    if request.method == 'POST':
        print(request.data['cart'])
        print(request.data)

        serializer = PlaceOrderSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            #print(serializer.data)
            user = User.objects.get(pk=serializer.data['user_id'])
            restaurant = Restaurant.objects.get(pk=serializer.data['restaurant_id'])
            print('----0000---0000---')
            print(int(serializer.data['delivery_address_id']))
            if(int(serializer.data['delivery_address_id'])>0):
                address = Address.objects.get(pk=serializer.data['delivery_address_id'])
            print('--------')
            print(user)
            print(restaurant)
            #print(address)
            print('========')
            print(serializer.data['coupon_discount_amount'],)
            print(serializer.data['coupon_discount_title'])
            print(serializer.data['order_amount'])
            print(serializer.data['order_type'])
            print(serializer.data['payment_method'])
            if(int(serializer.data['delivery_address_id'])>0):
                print(address.contact_person_name)
                print(str(address.contact_person_number))
                print(address.address)
                contact_person_name = address.contact_person_name,
                contact_person_phone = str(address.contact_person_number),
                delivery_address = address.address,
            else:
                contact_person_name = user.first_name+' '+user.last_name,
                contact_person_phone = 'nil',
                delivery_address = 'nil',
            print(serializer.data['payment_method'])
            print('---------')
            """
                user = user,
                restaurant = restaurant,

                coupon_discount_amount = 22.22,#serializer.data['coupon_discount_amount'],
                coupon_discount_title = 'SAT20',#serializer.data['coupon_discount_title'],
                order_amount = 200.12,#serializer.data['order_amount'],
                order_type = 'order type',#serializer.data['order_type'],
                payment_method = 'card',#serializer.data['payment_method'],
                contact_person_name = 'Mohammed',#address.contact_person_name,
                contact_person_phone = '08034902020',#address.contact_person_number,
                delivery_address = 'Gwarinpa, Abuja',#address.address,
                order_note = 'Cook fast',#serializer.data['order_note'],
                coupon_code = '09090'#serializer.data['coupon_code']
                
                #--------------------------------------------------
                """
            my_order = Order(
                user = user, restaurant = restaurant,

                coupon_discount_amount = 22.22,
                coupon_discount_title = 'SAT20',
                order_amount = 2000,
                order_type = 'order type',
                payment_method = 'card payment',
                #contact_person_name = 'mohammed Aliyu kkk',
                #contact_person_phone = '08034902025',
                #delivery_address = 'abuja',
                contact_person_name = contact_person_name,
                contact_person_phone = contact_person_phone,
                delivery_address = delivery_address,
                order_note = serializer.data['order_note'],
                coupon_code = 'coupon_code',
                order_status = 'pending'
            )
            my_order.save()
            print(my_order)
            print('---------')

            request.data['cart']
            #print('----'+request.data["cart"]["product_id"])
            product_id = 1 #int(request.data['cart']['product_id'])
            product_1 = Product.objects.get(id=1)
            product_2 = Product.objects.get(id=2)
            print(float(request.data['cart'][0]['price']))
            price = request.data['cart'][0]['price']
            discount_amount = 100.23#request.data['cart']['discount_amount']
            quantity = 1#request.data['cart']['quantity']
            

            my_order.products.add(product_1)
            my_order.products.add(product_2)
            print(product_1)
            print(product_2)
            
            """
            orderDetail = OrderDetail(
                order = my_order,
                order_status = 'pending',
                product = product_1,
                price = 123.23,
                discount_on_product = 100.23,
                quantity = 2.0,
                )
            """    


            #orderDetail.save()
            print(product_1.pk)
            print(product_2.pk)
            #orderDetail.product.add(product_1, product_2)
            

            #addon_ids = request.data['cart']['add_on_ids']
            data['message'] = "Successfully registered a new user."
            data['order_id'] = my_order.id
        
            #data['email'] = account.email
            #data['username'] = account.username
        else:
            print(serializer.errors)
            data = serializer.errors
        return Response(data)


@csrf_exempt
def user_register(request):
    now = datetime.datetime.now()
    print(request)
    if(request.method=='POST'):
        try:
            print(request.POST.get('first_name'))
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
    
    #djsh =  {
    #    cart: [
    #        {product_id: 3, price: 1500.0, variant: , 
    #            variation: [{type: null, price: null}], 
    #            discount_amount: 0.0, quantity: 1, tax_amount: 0.0, add_on_ids: [2], add_on_qtys: [1]}, 
            
            
            
    #        {product_id: 6, price: 2000.0, variant: , variation: [{type: null, price: null}], discount_amount: 0.0, quantity: 1, tax_amount: 0.0, add_on_ids: [2], add_on_qtys: [1]}, 
    #        {product_id: 5, price: 2000.0, variant: , variation: [{type: null, price: null}], discount_amount: 0.0, quantity: 1, tax_amount: 0.0, add_on_ids: [2], add_on_qtys: [1]}, 
    #        {product_id: 2, price: 4000.0, variant: , variation: [{type: null, price: null}], discount_amount: 0.0, quantity: 1, tax_amount: 0.0, add_on_ids: [2], add_on_qtys: [1]}
    #        ], 
    #        coupon_discount_amount: 0.0, 
    #        coupon_discount_title: null, 
    #        order_amount: 11500.0, 
    #        order_type: delivery, 
    #        delivery_address_id: 2, 
    #        payment_method: cash_on_delivery, 
    #        order_note: , 
    #        coupon_code: null}

    #        _user_id, order_amount, coupon_discount_amount, coupon_discount_title, payment_status, order_status, payment_method, 
    #       transaction_reference, delivery_address_id, delivery_man_id, delivery_charge, order_note, details_count, addons
            ####

    return HttpResponse(html)
    
