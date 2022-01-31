from django.shortcuts import render
from .models import Files, Project
from django.views.generic import DetailView


def file_home(request):
    file = Project.objects.order_by('-date')
    return render(request, 'files/file_home.html',{'file': file})


class FileDetailView(DetailView):
    model = Project
    template_name = 'files/file_details.html'
    context_object_name = 'files'