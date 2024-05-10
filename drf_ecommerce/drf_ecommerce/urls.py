from django.contrib import admin
from rest_framework.routers import DefaultRouter
from drf_ecommerce.product.views import CategoryViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
]
