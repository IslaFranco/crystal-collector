from django.contrib import admin

# Register your models here.
from .models import Crystal, Cleanse

admin.site.register(Crystal)
admin.site.register(Cleanse)