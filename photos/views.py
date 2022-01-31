from django.shortcuts import render, redirect
from .models import Photos, Project
from .forms import PhotoForm
from django.views.generic import DetailView


def phot_home(request):
    phot = Project.objects.order_by('-date')
    return render(request, 'photos/phot_home.html',{'phot': phot})


class PhotDetailView(DetailView):
    model = Project
    template_name = 'photos/phot_details.html'
    context_object_name = 'photos'