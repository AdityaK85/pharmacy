from .views import *
from django.urls import path
from . import views_ajax

simple_urls = [
    path('Dashboard', Dashboard, name='Dashboard'),
    path('Invoice', Invoice, name='Invoice'),
    path('Medicien', Medicien, name='Medicien'),
    path('Purchase', Purchase, name='Purchase'),
    path('Stock', Stock, name='Stock'),
    path('ManageStock', ManageStock, name='ManageStock'),
    path('StockReports', StockReports, name='StockReports'),
]

ajax_urls = [  
    
]
urlpatterns = [*simple_urls, *ajax_urls]