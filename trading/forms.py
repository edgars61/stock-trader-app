from django import forms

class InputNumeroForm(forms.Form):

    numero = forms.IntegerField()