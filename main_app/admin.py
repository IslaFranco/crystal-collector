from django.contrib import admin

# Register your models here.
from .models import Crystal, Cleanse, Blog

admin.site.register(Crystal)
admin.site.register(Cleanse)
admin.site.register(Blog)