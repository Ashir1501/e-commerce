from django.shortcuts import render, get_object_or_404
from .models import ProductModel, Category
from django.http import Http404
from django.db.models import Q
# Create your views here.
def home_page(request):
    all_data = ProductModel.objects.all()
    context = {
        'info': all_data
    }
    return render(request, 'index.html', context)

def product_details(request, id):
    product_detail = ProductModel.objects.get(id=id)
    context = {
        'product_info': product_detail
    }

    return render(request, 'product_detail.html', context)

def category_data(request, id):
    category_id = id
    category = get_object_or_404(Category, id = category_id)
    products = ProductModel.objects.filter(product_category = category_id)
    context = {
        'product_by_category' : products
    }

    return render(request, 'product_category_list.html', context)

def search_product(request):
    if request.method == 'GET':
        searched_data = request.GET.get('search')
        if(len(searched_data) == 0):
            raise Http404('pleasd provide valid seaRCH')
        else:
            # result = ProductModel.objects.filter(product_name__icontains = searched_data)
            result = ProductModel.objects.filter(Q(product_name__icontains = searched_data) | Q(product_description__icontains = searched_data))
            
            context = {
                'object': result
            }

            return render(request, 'search.html', context)
