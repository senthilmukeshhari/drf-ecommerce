from django.contrib import admin
from rest_framework.routers import DefaultRouter
from drf_ecommerce.product.views import CategoryViewSet, ProductViewSet, BrandViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path, include

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('brand', BrandViewSet, basename='brand')
router.register('product', ProductViewSet, basename='product')
urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]
