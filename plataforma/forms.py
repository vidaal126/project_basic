from django import forms
from plataforma.models import Livros


class Livro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = "__all__"
