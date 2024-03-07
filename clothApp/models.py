from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    
class ProductModel(models.Model):
    gender_option = (("M","Male"), ("F","Female"), ("B","Both"))
    product_name = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to='product_images', default=None)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gender = models.CharField(max_length=30, choices=gender_option)

    class Meta:
        db_table = 'Product'

    def __str__(self):
        return self.product_name
    