from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rainforest.models import Product, Review
from rainforest.forms import Product_Form

def root(request):
    return HttpResponseRedirect('home')

def home(request):
    product = Product.objects.all()
    context = {'prods': product}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def product_page(request, id):
    product_item = Product.objects.get(pk= int(id) )
    review = product_item.product.all()
    context ={'item': product_item, 'item_review': review}
    response = render(request, 'product.html', context)
    return HttpResponse(response)

def new_form(request):
    form_instance = Product_Form()
    context = {'form': form_instance}
    response = render(request, 'forms.html', context)
    return HttpResponse(response)
