from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage


def project_home(request):
    proj = Project.objects.order_by('-date')
    return render(request, 'projects/proj_home.html',{'proj': proj})


class ProjDetailView(DetailView):
    model = Project
    template_name = 'projects/proj_details.html'
    context_object_name = 'project'


class ProjUpdateView(UpdateView):
    model = Project  
    template_name = 'projects/create_proj.html'
    form_class = ProjectForm


class ProjDeleteView(DeleteView):
    model = Project
    success_url = '/projects/'
    template_name = 'projects/proj-delete.html' 


def create_proj(request):
    error = ''
    if request.method == 'POST':     
        form = ProjectForm(request.POST, request.FILES) 
        print("title = ",form)
        if form.is_valid():
            form.save()
            return redirect('proj_home')
        else:
            error = 'Некорректная форма.'    
    else:
        form = ProjectForm()
        
    data = { 'form': form,
        'error': error }

    return render(request,'projects/create_proj.html', data)