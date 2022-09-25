from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crystals/', views.crystals_index, name='index'),
    path('crystals/<int:crystal_id>/', views.crystals_detail, name='detail'),
    path('crystals/create/', views.CrystalCreate.as_view(), name='crystal_create'),
    path('crystals/<int:pk>/update/', views.CrystalUpdate.as_view(), name='crystal_update'),
    path('crystals/<int:pk>/delete/', views.CrystalDelete.as_view(), name='crystal_delete'),
    path('crystals/<int:crystal_id>/add_cleanse/', views.add_cleanse, name='add_cleanse'),
    path('blogs/', views.blogs_index, name='blog_index'),
    path('blogs/<int:blog_id>/', views.blogs_detail, name='blog_detail'),
    path('blogs/create/', views.BlogCreate.as_view(), name='blog_create'),
    path('blogs/<int:pk>/update/', views.BlogUpdate.as_view(), name='blog_update'),
    path('blogs/<int:pk>/delete/', views.BlogDelete.as_view(), name='blog_delete'),
    path('crystals/<int:crystal_id>/assoc_blog/<int:blog_id>/', views.assoc_blog, name='assoc_blog'),
    path('crystals/<int:crystal_id>/unassoc_blog/<int:blog_id>/', views.unassoc_blog, name='unassoc_blog'),
]
# DEfining view funcitons