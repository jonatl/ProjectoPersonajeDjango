from django import forms
from.models import contacto, Invocadore, Inventarie

class ContactameForm(forms.ModelForm):
    class Meta:
        model=contacto
        fields='__all__'

class InvocadorForm(forms.ModelForm):
    class Meta:
        model=Invocadore
        fields ='__all__'

class InventariooForm(forms.ModelForm):
    class Meta:
        model=Inventarie
        fields ='__all__'