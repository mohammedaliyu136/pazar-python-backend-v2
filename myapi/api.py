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

