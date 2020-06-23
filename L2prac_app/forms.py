from django import forms
from L2prac_app.models import Uinfo

class NewUserForm(forms.ModelForm):
    class Meta:
        model = Uinfo
        fields = '__all__'
        
