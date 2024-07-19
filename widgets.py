from django import forms
from django.forms import TimeInput
from django.forms import DateInput

class CustomTimeInput(TimeInput):
    input_type = 'time'
    format = '%H:%M'

class CustomDateInput(forms.DateInput):
    input_type = 'text'

    def __init__(self, attrs=None, format='%d-%m-%y'):
        super().__init__(attrs=attrs, format=format)

    def format_value(self, value):
        if isinstance(value, str):
            return value
        return value.strftime('%d-%m-%y') if value else ''