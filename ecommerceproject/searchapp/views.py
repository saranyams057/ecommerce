from django.shortcuts import render

# Create your views here.
from shopapp.models import Product
from django.db.models import Q


def Searchresult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains = query) | Q(discription__contains = query))
    return render(request, 'search.html', {'query': query, 'products': products})
