from django.db import models


class Livros(models.Model):
    nome_livro = models.CharField(max_length=70)
    decricao = models.TextField()
    n_paginas = models.IntegerField()

    def __str__(self) -> str:
        return self.nome_livro
