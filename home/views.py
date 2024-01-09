from django.shortcuts import render
from .models import Contact
from django.core.paginator import Paginator
import json
import random

#Read data json
f = open('data.json')
data = json.load(f)

PRODUCTS = data.get('products')
SERVICES = data.get('services')
product_list = []
[product_list.extend(i) for i in PRODUCTS.values() ]

class Product:

    def kitchen(request):
        return render(request, 'products.html', {'page_obj': pagination(request,PRODUCTS.get('kitchens'),6), 'section':'Cocinas'} )

    def doors(request):
        return render(request, 'products.html', {'page_obj': pagination(request,PRODUCTS.get('doors'),3), 'section':'Puertas para exteriores e interiores'} )
    
    def closet(request):
        return render(request, 'products.html', {'page_obj': pagination(request,PRODUCTS.get('closet'),3), 'section':'Vestieres Closet y Muebles de lino'} )
    
    def library(request):
        return render(request, 'products.html', {'page_obj': pagination(request,PRODUCTS.get('library'),3), 'section':'Bibliotecas y Centro de Entretenimiento','double_imgs':True} )

    def bathroom(request):
        return render(request, 'products.html', {'page_obj': pagination(request,PRODUCTS.get('bathroom'),3), 'section':'Muebles de bano'} )
    
    def stairs(request):
        return render(request, 'products.html', {'page_obj': pagination(request,PRODUCTS.get('stairs'),3), 'section':'Huellas para escalera en madera natural'} )
    
    def special_design(request):
        return render(request, 'products.html', {'page_obj': pagination(request,PRODUCTS.get('special_design'),3), 'section':'Diseño especiales'} )
    
class Services:

    def desing_and_fabrication(request):
        return render(request, 'products.html', {'page_obj': pagination(request,product_list,9), 'section':'Diseño y Fabricacion de mobiliario - Carpinteria'} )

    def tables_commercialization(request,type):
        return render(request, 'double_imgs.html', {'page_obj': SERVICES.get('tables_commercialization').get('imgs'), 'section':'Comercializacion y Suministro de Mesones o Ensimeras', 'url': '/servicios/comercializacion-y-suministro-de-mesones-o-ensimeras', 'type':type} )
    
    def hardware_commercialization(request,type):
        return render(request, 'services.html', {'page_obj': SERVICES.get('hardware_commercialization').get('imgs'), 'section':'Comercializacion y Suministro de Herraje para Mobiliario', 'type':type} )
       
def suppliers(request):
    return render(request,  'home.html')

def home(request):

        home = {'carousel': random.sample(product_list, 3),
                'products': random.sample(product_list, 6),
                'services': SERVICES }

        return render(request, 'home.html', home )
    
def about(request):
    return render(request,  'about.html')

def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['message']
        ins = Contact(name = name, email = email, phone = phone, desc = desc)
        ins.save()
    return render(request, 'contact.html')

def pagination(rq, item_list, item_numbers ):
    paginator = Paginator(item_list, item_numbers)
    page_number = rq.GET.get("page")
    page_obj = paginator.get_page(page_number)      
    return page_obj

def all_products(request):
    return render(request, 'products.html', {'page_obj': pagination(request,product_list,9), 'section':'Todos los productos'} )