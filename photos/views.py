from django.shortcuts import render, redirect
from .models import Photos
from .forms import PhotoForm
from django.views.generic import DetailView, UpdateView, DeleteView


def phot_home(request):
    phot = Photos.objects.order_by('-date')
    return render(request, 'photos/phot_home.html',{'phot': phot})


class PhotDetailView(DetailView):
    model = Photos
    template_name = 'photos/phot_details.html'
    context_object_name = 'photos'


class PhotUpdateView(UpdateView):
    model = Photos 
    success_url = '/photos/'
    template_name = 'photos/phot_create.html'     
    form_class = PhotoForm


class PhotDeleteView(DeleteView):
    model = Photos
    success_url = '/photos/'
    template_name = 'photos/phot-delete.html' 


def create_phot(request):
    error = ""
    if request.method=='POST':        
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():            
            form.save()
            return redirect('phot_home')
        else:
            error = "Форма некорректна"
    else:            
        form = PhotoForm()            

    context = { 'form': form,
    'error': error }

    return render(request,'photos/phot_create.html', context)