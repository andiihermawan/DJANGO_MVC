from django.shortcuts import render

def Home(request):
    return render (request, 'Home/home.html', {})

# Create your views here.