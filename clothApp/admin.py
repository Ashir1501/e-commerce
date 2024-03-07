from django.contrib import admin
from .models import Category, ProductModel
from django.utils.html import format_html
from accounts.models import Account
# Register your models here.

class CustomProduct(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'gender', 'product_description', 'img_display']
    list_per_page = 5
    list_filter = ['gender', 'product_price']
    search_fields = ['product_name']

    def img_display(self, obj):
        return format_html("<img src='{}' width='90' height='100' />", obj.product_image.url)

admin.site.register(Category)
admin.site.register(ProductModel, CustomProduct)
admin.site.register(Account)

admin.site.site_header = 'Cloth Store Applicaton'
admin.site.index_title = 'Cloth Store Admin'