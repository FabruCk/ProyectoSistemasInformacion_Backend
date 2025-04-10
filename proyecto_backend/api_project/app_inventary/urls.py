from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserProfileViewSet, CategoryViewSet, SupplierViewSet,
    ProductViewSet, InventoryMovementViewSet
)

router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)
router.register(r'inventory-movements', InventoryMovementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

