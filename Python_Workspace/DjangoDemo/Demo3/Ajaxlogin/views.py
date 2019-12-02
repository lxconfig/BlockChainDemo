from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def login(request):
    return render(request, 'Ajaxlogin/login.html')

def login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    # username = request.GET.get('username')
    # password = request.GET.get('password')

    if username == 'lixuan' and password == '123':
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})

def index(request):
    return render(request, 'Ajaxlogin/index.html')
