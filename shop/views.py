from ast import Pass
from collections import OrderedDict
import json
from math import ceil
from turtle import update
from urllib import response
from django.shortcuts import render   # ue for rendering the page like basic.hmtl etc
from django.http import HttpResponse  #use for display text
from .models import Order, OrderUpdate, product ,Contact

# Create your views here.
def index(request):
    # products=product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides= n//4 + ceil((n/4)-(n//4))
    # #params ={'no_of_slides':nSlides ,'range':range(1,nSlides), 'product': products}     # show all products
    # allprod = [[products, range(1,nSlides) , nSlides],
    #            [products, range(1, nSlides) , nSlides]]
    allprod =[]
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods }
    for cat in cats:                                                     # show categories wise products
        prod =product.objects.filter(category=cat)                       #fatch the product name category
        n= len(prod)
        nSlides= n//4 + ceil((n/4)-(n//4))
        allprod.append([prod, range(1,nSlides), nSlides])

    params ={'allprod':allprod}                  #params is dictonary
    return render(request,'shop/index.html', params)

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    if request.method=="POST":
        name= request.POST.get('name', '')
        email= request.POST.get('email', '')                              #fatching data from contact.html and  send to superuser
        phone= request.POST.get('phone', '')
        desc= request.POST.get('desc', '')
        contact=Contact(name=name,email=email, phone=phone,desc=desc)
        contact.save()
    return render(request, "shop/contact.html")

def tracker(request):
    if request.method=="POST":
        orderId= request.POST.get('orderId', '')
        email= request.POST.get('email', '')
        try: 
            orders =Order.objects.filter(order_id=orderId,email=email)
            if len(orders)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates,orders[0].items_json],default=str)  #for display items in tracker
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request,"shop/tracker.html")

def search(request):
    return render(request,"shop/search.html")

def productview(request,myid):
    #fatching the product using the myid
    Product = product.objects.filter(id=myid)
    print(Product)

    return render(request,"shop/productview.html",{'product':Product[0]})     #product= we have acess in productview.html or Product= acess form  Product.object.filter(id=myid)

def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsjson', '')
        name= request.POST.get('name', '')
        email= request.POST.get('email', '')
        address= request.POST.get('address', '')                          #fatching data from contact.html and  send to superuser
        phone= request.POST.get('phone', '')
        city= request.POST.get('city', '')
        state= request.POST.get('state', '')
        zip_code= request.POST.get('zip_code', '')
        checkout=Order(items_json=items_json,  name=name, email=email, address=address, phone=phone, city=city, state=state,zip_code=zip_code)
        checkout.save()
        update = OrderUpdate(order_id=checkout.order_id, update_desc="The Order has been placed")
        update.save()
        thank = True
        id = checkout.order_id
        return render(request,"shop/checkout.html" ,{'thank':thank ,'id':id })   #after submition cart become empty

    return render(request,"shop/checkout.html")