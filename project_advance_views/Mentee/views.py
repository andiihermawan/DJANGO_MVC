from django.shortcuts import render
from .models import Mentee

# Create your views here.
def MenteePost(request):
    mentee = Mentee.objects.all()
    return render(request, 'Mentee/mentee.html',{'mentee':mentee})

