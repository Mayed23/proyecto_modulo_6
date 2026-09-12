from django import forms
from datetime import date
from .models import Proyecto, Tarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = [
            'nombre',
            'descripcion',
        ]


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = [
            'titulo',
            'estado',
            'prioridad',
            'fecha_limite',
            'asignado_a',
        ]
        widgets = {
            'fecha_limite': forms.DateInput(
                attrs={'type': 'date'}
            )
        }

    def clean_fecha_limite(self):
        fecha_limite = self.cleaned_data.get('fecha_limite')
        if fecha_limite and fecha_limite < date.today():
            raise forms.ValidationError(
                "La fecha límite no puede ser anterior a hoy."
            )
        return fecha_limite


class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='Nombre')
    last_name = forms.CharField(max_length=30, required=True, label='Apellido')
    email = forms.EmailField(required=True, label='Correo electrónico')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
