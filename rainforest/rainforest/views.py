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
