from django.http import HttpResponse
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

# def new_form(request):
#     form_instance = Product_Form()
#     context = {'form': form_instance}
#     response = render(request, 'forms.html', context)
#     return HttpResponse(response)
#
# def post_form(request):
#     picture = Picture.objects.get(pk= request.POST['picture'])
#     comment = picture.comments.create(name=request.POST['name'],
#     message=request.POST['comment']
#     )
#     return HttpResponseRedirect('/pictures/{}'.format(picture.pk))

def new_form(request):
    if request.method == 'POST':
        form = Product_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = Product_Form()
        context = {'form': form}
        return render(request, 'forms.html', context)
