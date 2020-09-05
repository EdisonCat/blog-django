from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
def products_view(request, *args, **kwargs):
    products_list = Product.objects.all()
    context = {
        'products_list': products_list
    }
    return render(request, "products.html", context)

def products_detail_view(request, my_id):
    # return render(request,"product/detail.html", {})
    # obj = get_object_or_404(Product, id=my_id)
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        'object': obj
    }
    return render(request, "products_detail.html", context)

def products_create_view(request, *args, **kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid(): 
        print(form.cleaned_data)
        Product.objects.create(**form.cleaned_data)

    # form = RawProductForm()
    # if request.method == "POST":
    #     form = RawProductForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         Product.objects.create(**form.cleaned_data)
    #     else:
    #         print(form.errors)
    context = {
        'form': form
    }
    return render(request, "products_create.html", context)

def products_delete_view(request, my_id):
    obj = get_object_or_404(Product, id = my_id)
    if request.method == "POST" :
        obj.delete()
        link = '../../products/'+str(my_id)+'/delete_success'
        print(link)
        return redirect(link)
    context = {
        "object": obj
    }
    return render(request, "products_delete.html", context)

def products_delete_success(request, my_id):
    context = {
        'id': my_id
    }
    return render(request, "products_delete_success.html", context)