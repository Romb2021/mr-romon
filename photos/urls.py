from django.urls import path
from . import views

urlpatterns = [    
    path('', views.phot_home, name='phot_home'),    
    path('<int:pk>', views.PhotDetailView.as_view() , name='phot_detail')
]