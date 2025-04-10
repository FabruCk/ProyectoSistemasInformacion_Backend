from django.db import models
from django.contrib.auth.models import User
# modelos test github probando las ramas
# Usuario a iniciar el manejo (Administrador, Empleado, Supervisor)
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('empleado', 'Empleado'),
        ('supervisor', 'Supervisor'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Categoría de producto (ej: Computadores, Celulares)
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Proveedor de productos
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Producto del inventario
class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, related_name='products')
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.brand} {self.model})"

# Movimiento de inventario (entrada o salida)
class InventoryMovement(models.Model):
    MOVEMENT_TYPE = (
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='movements')
    type = models.CharField(max_length=10, choices=MOVEMENT_TYPE)
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    note = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type.title()} - {self.product.name} ({self.quantity})"

    def save(self, *args, **kwargs):
        if self.pk is None:  # Solo ajustar stock si es nuevo
            if self.type == 'entrada':
                self.product.stock += self.quantity
            elif self.type == 'salida':
                self.product.stock -= self.quantity
            self.product.save()
        super().save(*args, **kwargs)
