from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rainforest.models import Product, Review

def root(request):
    return HttpResponseRedirect('home')

def home(request):
    product = Product.objects.all()
    context = {'prods': product}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def product_page(request, id):
    product_item = Product.objects.get(pk= int(id) )
    context ={'item': product_item}
    response = render(request, 'product.html', context)
    return HttpResponse(response)
