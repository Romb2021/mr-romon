from django.urls import path
from . import views

urlpatterns = [    
    path('', views.phot_home, name='phot_home'),
    path('phot_create', views.create_phot, name='phot_create'),
    path('<int:pk>', views.PhotDetailView.as_view() , name='phot_detail'),    
    path('<int:pk>/update', views.PhotUpdateView.as_view() , name='phot_update'),
    path('<int:pk>/delete', views.PhotDeleteView.as_view() , name='phot_delete')
]