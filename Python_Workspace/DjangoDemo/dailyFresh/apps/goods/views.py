from django.shortcuts import render

# Create your views here.

# /goods/index
def index(request):
    return render(request, 'index.html')