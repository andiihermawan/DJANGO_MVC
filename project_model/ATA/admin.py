from django.contrib import admin
from .models import Direksi,Mentee,Mentor,Mata_pelajaran,Challenge,Live_Code

my_model = [Direksi,Mentee,Mentor,Mata_pelajaran,Challenge,Live_Code]
admin.site.register(my_model)

# Register your models here.
