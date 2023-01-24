from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import JsonResponse
from category.models import Category


from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
register = template.Library()

from carts.views import _cart_id
from django.http import HttpResponse
from carts.models import CartItem
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

def store(request, category_slug=None):

    '''
    categories = None
    products = None

    if category_slug != None:
        categories =get_object_or_404(Category, slug = category_slug)   
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

        product_count =products.count()

        
    else:

        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

        product_count =products.count()
    '''
    #categories = get_object_or_404(Category, slug = category_slug)   
    products = Product.objects.all().filter(is_available=True).order_by('id')
    paginator = Paginator(products, 1)
    first_page = paginator.page(1).object_list
    page_range = paginator.page_range

    product_count = products.count()

    context ={
        'products': first_page,
        'paginator': paginator,
        'product_count' : product_count,
        'first_page': first_page,
        'page_range': page_range,
    }

    if request.method == 'POST':

        page_n = request.POST.get('page_n', None)
        vals = ["id", "product_name", "slug", "description", "price", "stock", "image", "is_available", "category"
]
        results = list(paginator.page(page_n).object_list.values("id", "product_name", "slug", "description", "price", "stock", "image", "is_available", "category"))      
        
        product = products.filter(id=paginator.page(page_n).object_list.values('id')[0]['id'])
        results[0]["product_url"] = product[0].get_url()
        results[0]["image_url"] = product[0].image.url
        
        print(results)
        
        print(JsonResponse({ "results": results }))
        return JsonResponse({ "results": results })


    return render(request, 'store/store.html', context)



@register.simple_tag
def my_tag(a, b):
    
    return '<b>Noman</b>'



def product_detail(request, category_slug, product_slug):

    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)

        in_cart =CartItem.objects.filter(cart__cart_id = _cart_id(request), product =single_product).exists() 
        #to check already added in cart or not
       
    except Exception as e:
        raise e
    context = {
        'single_product' : single_product,
        'in_cart':in_cart,
    }
    return render(request, 'store/product_detail.html',context)