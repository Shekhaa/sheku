from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [ 
    path('index',views.index, name="home"),
    path('Carts',views.Carts,name="Carts")
    
]
