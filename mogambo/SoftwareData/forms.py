from django import forms
from .models import Software, Rating


class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ('name', "user", "icon", 'version',  'weburl',
                  'description', 'category', )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'form-control-file'}),
            'version': forms.TextInput(attrs={'class': 'form-control'}),
            'weburl': forms.URLInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),

        }
