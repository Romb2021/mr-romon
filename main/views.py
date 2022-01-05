from django.shortcuts import render

def index(request):
    data = {
        'title':'Главная страница'
    }
    return render(request,'main/index.html',data)     


def contact(request):
    return render(request,'main/contact.html')    