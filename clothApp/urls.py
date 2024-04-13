from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('product-detail/<int:id>/', views.product_details, name='product-detail'),
    path('category/<int:id>/', views.category_data, name='category_data'),
    path('search/',views.search_product, name='search'),
    path('services/',views.services, name='services'),
]