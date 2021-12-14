from django.urls import path, re_path
from . import views

urlpatterns = [    
    path('', views.project_home, name='proj_home'),
    path('create_proj', views.create_proj, name='create_proj'),
    path('<int:pk>', views.ProjDetailView.as_view(), name='detail_proj'),
    path('<int:pk>/update', views.ProjUpdateView.as_view(), name='update_proj'),
    path('<int:pk>/delete', views.ProjDeleteView.as_view(), name='delete_proj')
]