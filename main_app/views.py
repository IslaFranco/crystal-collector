from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Crystal
from .forms import CleanseForm

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
    cleanse_form = CleanseForm()
    return render(request, 'crystals/detail.html', {
        'crystal': crystal,
        'cleanse_form': cleanse_form
        })

def add_cleanse(request, crystal_id):
    form = CleanseForm(request.POST) 

    if form.is_valid():
      new_cleanse = form.save(commit=False)      
      new_cleanse.crystal_id = crystal_id
      new_cleanse.save()
    return redirect('detail', crystal_id=crystal_id) 

class CrystalCreate(CreateView):
    model = Crystal
    fields = '__all__'  
    # success_url = '/crystals/'  

class CrystalUpdate(UpdateView):
    model = Crystal
    fields = ('description', 'properties', 'chakras', 'zodiac', 'color') 

class CrystalDelete(DeleteView):
    model = Crystal
    success_url = '/crystals/'    

