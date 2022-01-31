from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    data = {
        'title':'Главная страница'
    }
    return render(request,'main/index.html',data)     

def get_suzer(request):
    susers = User.objects.filter(is_superuser=True)  
    data = {
        'title':'Cтраница вывода суперюзеров',
        'susers': susers}
    return render(request,'main/get_suzer.html',data)       

def contact(request):
    return render(request,'main/contact.html')    