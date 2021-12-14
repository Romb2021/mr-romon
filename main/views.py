from django.shortcuts import render

def index(request):
    data = {
        'title':'Главная страница'
        # 'values':['Some','Hello','123'],
        # 'obj': {
        #    'car': 'BMV',
        #    'age': 18,
        #    'hobby': 'Football'         }
    }
    return render(request,'main/index.html',data)


def photo(request):
    return render(request,'main/photo.html')     

def files(request):
    return render(request,'main/files.html')     

def contact(request):
    return render(request,'main/contact.html')    