from django.shortcuts import render
from .models import Files
from django.views.generic import DetailView


def file_home(request):
    file = Files.objects.order_by('-date')
    return render(request, 'files/file_home.html',{'file': file})


class FileDetailView(DetailView):
    model = Files
    template_name = 'files/file_details.html'
    context_object_name = 'files'