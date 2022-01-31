from django.urls import path
from . import views

urlpatterns = [    
    path("", views.index, name='home'),        
    path('contact',views.contact, name='contact'),
    path('suzer',views.get_suzer, name='suzer') 
]