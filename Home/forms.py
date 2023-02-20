from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput,PasswordInput
from django.contrib.auth.models import User

class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name","email","username","password1","password2"]
        
        widgets = {
            'username': TextInput(attrs={'class': 'form-control','placeholder':'User Name'}),
            'first_name': TextInput(attrs={'class': 'form-control','placeholder':'First Name'}),
            'last_name': TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}),
            'email': TextInput(attrs={'class': 'form-control','placeholder':'Email Id'}),
            "password1": PasswordInput(attrs={'class': 'form-control','placeholder':'Email Id'})

        }