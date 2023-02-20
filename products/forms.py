from django.forms import ModelForm,TextInput
from .models import Products

class ProductAddForm(ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        
        widgets = {
            'Expairy_Date': TextInput(attrs={"type":"date"}),
        }