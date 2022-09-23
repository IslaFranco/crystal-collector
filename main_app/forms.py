from copyreg import clear_extension_cache
from django.forms import ModelForm
from .models import Cleanse

class CleanseForm(ModelForm):
    class Meta:
        model = Cleanse
        fields = ('date', 'method')