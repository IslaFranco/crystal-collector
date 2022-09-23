from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crystals/', views.crystals_index, name='index'),
    path('crystals/<int:crystal_id>/', views.crystals_detail, name='detail'),
    path('crystals/create/', views.CrystalCreate.as_view(), name='crystal_create'),
]
# DEfining view funcitons