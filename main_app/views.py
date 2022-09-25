from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Crystal
from .models import Blog
from .forms import CleanseForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {'page_name': 'Home'})

def about(request):
    return render(request, 'about.html')       

@login_required
def crystals_index(request):
    crystals = Crystal.objects.filter(user=request.user)
    return render(request, 'crystals/index.html', { 'crystals': crystals })

@login_required
def crystals_detail(request, crystal_id):
    crystal = Crystal.objects.get(id=crystal_id)
    cleanse_form = CleanseForm()
    blogs_crystal_doesnt_have = Blog.objects.exclude(id__in = crystal.blogs.all().values_list('id'))
    return render(request, 'crystals/detail.html', {
        'crystal': crystal,
        'cleanse_form': cleanse_form,
        'blogs': blogs_crystal_doesnt_have
        })
@login_required
def add_cleanse(request, crystal_id):
    form = CleanseForm(request.POST) 

    if form.is_valid():
      new_cleanse = form.save(commit=False)      
      new_cleanse.crystal_id = crystal_id
      new_cleanse.save()
    return redirect('detail', crystal_id=crystal_id) 

@login_required
def assoc_blog(request, crystal_id, blog_id):
    Crystal.objects.get(id=crystal_id).blogs.add(blog_id)  
    return redirect('detail', crystal_id=crystal_id)  

def unassoc_blog(request, crystal_id, blog_id):
    Crystal.objects.get(id=crystal_id).blogs.remove(blog_id)  
    return redirect('detail', crystal_id=crystal_id) 

def signup(request):
    form = UserCreationForm()
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid response'
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)          

class CrystalCreate(LoginRequiredMixin, CreateView):
    model = Crystal
    fields = ('name', 'description', 'properties', 'chakras', 'zodiac', 'color',) 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) 
    # success_url = '/crystals/'  

class CrystalUpdate(LoginRequiredMixin, UpdateView):
    model = Crystal
    fields = ('description', 'properties', 'chakras', 'zodiac', 'color') 

class CrystalDelete(LoginRequiredMixin, DeleteView):
    model = Crystal
    success_url = '/crystals/'  

def blogs_index(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/index.html', {'blogs': blogs })

def blogs_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog':blog })

class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blog
    fields = '__all__' 

class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('content',)    

class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = '/blogs/'               

