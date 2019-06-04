from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from rainforest.models import Product, Review
from rainforest.forms import Product_Form
# import ipdb

def root(request):
    return HttpResponseRedirect('home')

def test(request):
    response = render(request, 'test.html')
    return HttpResponse(response)

def home(request):
    product = Product.objects.all().order_by('-id')
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
    if request.method == 'POST':
        form = Product_Form(request.POST)
        if form.is_valid():
            new_product = form.save()
            return HttpResponseRedirect('/product/'+ str(new_product.pk))
        else:
            raise Http404
    else:
        form = Product_Form()
    return render(request, 'forms.html', {'form': form})
