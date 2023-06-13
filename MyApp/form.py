from django import forms
from .models import Tarea



class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'fecha_cumplimiento', 'completada']
        widgets = {
            'completada': forms.CheckboxInput(attrs={'value': True}),
        }
