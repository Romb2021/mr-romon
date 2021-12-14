from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache
from django.conf.urls.static import static

urlpatterns = [    
    path("", views.index, name='home'),        
    path('photo',views.photo, name='photo'),
    path('files',views.files, name='files'),
    path('contact',views.contact, name='contact') 
]