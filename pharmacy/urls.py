from .views import *
from django.urls import path
from . import views_ajax

simple_urls = [
    
]

ajax_urls = [  
    
]
urlpatterns = [*simple_urls, *ajax_urls]