from django import forms
from .models import *
from django.core.exceptions import ValidationError


class userprofileform(forms.ModelForm):
    class Meta:
        model=userprofile
        fields='__all__'
class toysform(forms.ModelForm):
    class Meta:
        model=toys
        fields='__all__'

class vehicleform(forms.ModelForm):
    class Meta:
        model=vehicle
        fields='__all__'
class registrationform(forms.ModelForm):
    class Meta:
        model=registrtation
        fields='__all__'        
    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) <= 5:
            raise forms.ValidationError("Password must be more than 5 characters.")
        
        return password

class houseform(forms.ModelForm):
    class Meta:
        model=house
        fields='__all__'    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) <= 3:
            raise forms.ValidationError("Name must be more than three characters")
        return name
    
class login1form(forms.ModelForm):
    class Meta:
        model=login1
        fields='__all__'

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) <= 5:
            raise ValidationError("Password must be more than five characters long.")
        return password
    
