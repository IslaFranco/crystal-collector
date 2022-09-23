from django.shortcuts import render
from .models import Crystal

# Create your views here.
def home(request):
    return render(request, 'home.html', {'page_name': 'Home'})

def about(request):
    return render(request, 'about.html')       

def crystals_index(request):
    crystals = Crystal.objects.all()
    return render(request, 'crystals/index.html', { 'crystals': crystals })

def crystals_detail(request, crystal_id):
    crystal = Crystal.objects.get(id=crystal_id)
    return render(request, 'crystals/detail.html', {'crystal': crystal})
