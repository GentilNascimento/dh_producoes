from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator
from validate_docbr import CPF # type: ignore
from django.utils.translation import gettext_lazy as _

# Lista de opções de tipo de chave PIX
TIPO_CHAVE_CHOICES = [
    ('cel', 'Celular'),
    ('cnpj', 'CNPJ'),
    ('email', 'E-mail'),
    ('cpf', 'CPF'),
]

# Aqui vão as definições de modelos existentes, como Artista, etc.

def validar_cpf(value):
    cpf_validator = CPF()
    if not cpf_validator.validate(value):
        raise ValidationError('CPF inválido.')


def validar_chave_pix(value, tipo_chave):
    if tipo_chave == 'cel':  # Verifica se a chave PIX é um número de celular
        if len(value) != 11 or not value.isdigit():
            raise ValidationError('O número de celular deve conter exatamente 11 dígitos numéricos.')
    elif tipo_chave == 'cnpj':  # Verifica se a chave PIX é um CNPJ
        if len(value) != 14 or not value.isdigit():
            raise ValidationError('O CNPJ deve conter exatamente 14 dígitos numéricos.')
    elif tipo_chave == 'email':  # Verifica se a chave PIX é um e-mail
        validator = EmailValidator(message='O e-mail fornecido não é válido.')
        validator(value)
    else:
        raise ValidationError('Tipo de chave PIX inválido.')
    
def validar_horario(value):
    # Verifica se o horário é '24:00' horas
    if value.hour == 0 and value.minute == 0:
        return
    # Verifica se o horário está dentro do intervalo válido (por exemplo, entre 00:00 e 23:59)
    if value < datetime.time(0, 0) or value > datetime.time(23, 59):
        raise ValidationError('Horário inválido. O horário deve estar entre 00:00 e 23:59.')
    
class Artista(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, unique=True, validators=[validar_cpf])
    telefone = models.CharField(max_length=15, null=True)
    banco = models.CharField(max_length=100, null=True)  #instituição bancária
    tipo_chave_pix = models.CharField(max_length=10, choices=TIPO_CHAVE_CHOICES, default='cel')
    chave_pix = models.CharField(max_length=100)
    
    def clean(self):
        validar_chave_pix(self.chave_pix, self.tipo_chave_pix)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField(validators=[validar_horario])
    
    def __str__(self):
        return self.artista.nome if self.artista else 'Evento sem artista'
    # Adicione outros campos relevantes para os eventos, se necessário

     

