from django.shortcuts import render
from .models import Mentor

# Create your views here.
def MentorPost(request):
    mentor = Mentor.objects.all()
    return render(request, 'Mentor/mentor.html',{'mentor':mentor})

