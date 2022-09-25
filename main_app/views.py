from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Crystal
from .models import Blog
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
    blogs_crystal_doesnt_have = Blog.objects.exclude(id__in = crystal.blogs.all().values_list('id'))
    return render(request, 'crystals/detail.html', {
        'crystal': crystal,
        'cleanse_form': cleanse_form,
        'blogs': blogs_crystal_doesnt_have
        })

def add_cleanse(request, crystal_id):
    form = CleanseForm(request.POST) 

    if form.is_valid():
      new_cleanse = form.save(commit=False)      
      new_cleanse.crystal_id = crystal_id
      new_cleanse.save()
    return redirect('detail', crystal_id=crystal_id) 

def assoc_blog(request, crystal_id, blog_id):
    Crystal.objects.get(id=crystal_id).blogs.add(blog_id)  
    return redirect('detail', crystal_id=crystal_id)  

class CrystalCreate(CreateView):
    model = Crystal
    fields = ('name', 'description', 'properties', 'chakras', 'zodiac', 'color',)  
    # success_url = '/crystals/'  

class CrystalUpdate(UpdateView):
    model = Crystal
    fields = ('description', 'properties', 'chakras', 'zodiac', 'color') 

class CrystalDelete(DeleteView):
    model = Crystal
    success_url = '/crystals/'  

def blogs_index(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/index.html', {'blogs': blogs })

def blogs_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog':blog })

class BlogCreate(CreateView):
    model = Blog
    fields = '__all__' 

class BlogUpdate(UpdateView):
    model = Blog
    fields = ('content',)    

class BlogDelete(DeleteView):
    model = Blog
    success_url = '/blogs/'               

