from django import forms
from .models import ObjetoPerdido, Comentario

class ObjetoForm(forms.ModelForm):
    class Meta:
        model = ObjetoPerdido
        fields = ['titulo', 'descripcion', 'encontrado']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows':2, 'placeholder':'¿Tienes información adicional?'}),
        }
