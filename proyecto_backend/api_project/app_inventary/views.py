from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import UserProfile, Category, Supplier, Product, InventoryMovement
from .serializers import (
    UserProfileSerializer, CategorySerializer,
    SupplierSerializer, ProductSerializer, InventoryMovementSerializer
)
from rest_framework.permissions import IsAuthenticated

def index(request):
    return HttpResponse("Inventario funcionando")


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = []

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = []

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []

class InventoryMovementViewSet(viewsets.ModelViewSet):
    queryset = InventoryMovement.objects.all()
    serializer_class = InventoryMovementSerializer
    permission_classes = []
