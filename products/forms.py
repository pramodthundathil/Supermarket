from django.forms import ModelForm,TextInput
from .models import Products,Venders

class ProductAddForm(ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        
        widgets = {
            'Expairy_Date': TextInput(attrs={"type":"date"}),
        
        }
        
class Venderaddfrom(ModelForm):
    class Meta:
        model = Venders
        fields = ["Vender_name","Vender_Poducts","Vender_Product_Cat"]