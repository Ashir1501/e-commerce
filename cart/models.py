from django.db import models
from clothApp.models import ProductModel
from accounts.models import Account
# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add = True)

    @property
    def cost_per_item(self):
        return self.quantity * self.product.product_price

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name}"

class Cart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name='cart')
    session_key = models.CharField(max_length=50, null=True, blank=True)
    items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.email if self.user else 'Guest'}"
    