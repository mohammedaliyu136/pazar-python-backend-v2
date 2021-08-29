from rest_framework import routers
from restaurant import views as restaurant_views
from account import views as account_views

router = routers.DefaultRouter()
router.register(r'restaurants', restaurant_views.RestaurantViewSet)
router.register(r'products', restaurant_views.ProductViewSet)
router.register(r'variations', restaurant_views.VariationViewSet)
router.register(r'addons', restaurant_views.AddOnsViewSet)
router.register(r'choice-options', restaurant_views.ChoiceOptionViewSet)
router.register(r'categories', restaurant_views.CategoryViewSet)
router.register(r'option', restaurant_views.OptionViewSet)
router.register(r'banners', restaurant_views.BannerViewSet)
router.register(r'users', account_views.Userviewsets)
router.register(r'address', account_views.Addressviewsets)
router.register(r'profile', account_views.Profileviewsets)
router.register(r'config', account_views.Configviewsets)
router.register(r'product-wish-list', restaurant_views.ProductWishListViewSet)
router.register(r'restaurant-wish-list', restaurant_views.RestaurantWishListViewSet)
router.register(r'order-list', restaurant_views.OrderViewSet)
router.register(r'order-detail', restaurant_views.OrderDetailViewSet)
router.register(r'coupon', restaurant_views.PromoCodeViewSet)


""""
[
    {
        'product_id': '5', 'price': '2000.0', 'variant': '', 
        'variation': [
            {'type': None, 'price': None}
            ], 
        'discount_amount': 0.0, 'quantity': 1, 
        'tax_amount': 0.0, 'add_on_ids': [1], 'add_on_qtys': [1]}]
2021-08-27T09:08:15.314154+00:00 app[web.1]: {'cart': [{'product_id': '5', 'price': '2000.0', 'variant': '', 'variation': [{'type': None, 'price': None}], 'discount_amount': 0.0, 'quantity': 1, 'tax_amount': 0.0, 'add_on_ids': [1], 'add_on_qtys': [1]}], 'coupon_discount_amount': 0.0, 'coupon_discount_title': 'none', 'order_amount': 2200.0, 'order_type': 'delivery', 'delivery_address_id': 4, 'payment_method': 'cash_on_delivery', 'order_note': '', 'coupon_code': 'none', 'user_id': '2', 'restaurant_id': '1', 'payment_status': '1', 'order_status': '1', 'transaction_reference': '1', 'delivery_charge': '1', 'details_count': 1, 'addon_id': 'none'}
2021-08-27T09:08:15.315174+00:00 app[web.1]: {'user_id': '2', 'restaurant_id': '1', 'order_amount': '2200.0', 'coupon_discount_amount': '0.0', 'coupon_discount_title': 'none', 'payment_status': '1', 'order_status': '1', 'payment_method': 'cash_on_delivery', 'transaction_reference': '1', 'delivery_address_id': '4', 'delivery_charge': '1', 'order_note': '', 'details_count': '1', 'addon_id': 'none', 'order_type': 'delivery'}
"""

