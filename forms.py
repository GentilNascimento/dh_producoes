from django import forms
from .models import Artista, Evento
from .widgets import CustomDateInput
class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = '__all__'  # Utilize '__all__' para incluir todos os campos do modelo no formulário
        
class CustomDateInput(forms.DateInput):
    input_type = 'text'

    def __init__(self, attrs=None, format='%d-%m-%y'):
        super().__init__(attrs=attrs, format=format)

    def format_value(self, value):
        if isinstance(value, str):
            return value
        return value.strftime('%d-%m-%y') if value else ''


class EventoForm(forms.ModelForm):
    data = forms.DateField(widget=CustomDateInput, input_formats=['%d-%m-%Y', '%d-%m-%y'])
    horario = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    class Meta:
        model = Evento
        fields = ['artista', 'data', 'horario']
        
    