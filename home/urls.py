from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Developer Paula otro'
admin.site.site_title = "Welcome to Paula's Dashboard"
admin.site.index_title = 'Welcome to this portal'

urlpatterns = [
    path('', views.home, name='home'),
    path('nosotros', views.about, name='about'),
    path('proveedores', views.home, name='suppliers'),
    path('contacto', views.contact, name='contact'),
    path('todos-productos', views.all_products, name='all_products'),
    path("servicios/",
        include(
            [
                path("diseno-y-fabricacion-de-mobiliario-carpinteria", views.Services.desing_and_fabrication, name='sr_desing_and_fabrication'),
                path("comercializacion-y-suministro-de-mesones-o-ensimeras/<str:type>", views.Services.tables_commercialization, name='sr_tables_commercialization'),
                path("comercializacion-y-suministro-de-herraje-para-mobiliario/<str:type>",views.Services.hardware_commercialization, name='sr_hardware_commercialization')
            ]
        ),
    ),
    path("productos/",
        include(
            [
                path("cocinas", views.Product.kitchen, name='pr_kitchen'),
                path("puertas-para-exteriores-e-interiores", views.Product.doors, name='pr_doors'),
                path("vestieres-closet-y-muebles-de-lino",views.Product.closet, name='pr_closet'),
                path("bibliotecas-y-centro-de-entretenimiento", views.Product.library, name='pr_library'),
                path("muebles-para-banos", views.Product.bathroom, name='pr_bathroom'),
                path("huellas-para-escalera-en-madera-natural", views.Product.stairs, name='pr_stairs'),
                path("diseno-especiales", views.Product.special_design, name='pr_special_design')
            ]
        ),
    )
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)