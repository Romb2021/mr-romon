from django.urls import path
from . import views

urlpatterns = [    
    path('', views.file_home, name='file_home'),    
    path('<int:pk>', views.FileDetailView.as_view() , name='file_details')
]