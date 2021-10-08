"""receitas Models"""

# Componentes do Django
from django.db import models
# Componentes de outros módulos
from fractions import Fraction


class Tag(models.Model):
    nome = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome


class Ingrediente(models.Model):
    quantidade = models.FloatField()
    quantificador = models.CharField(max_length=20, blank=True)
    produto_ingrediente = models.ForeignKey(Produto, on_delete=models.PROTECT)

    def __str__(self):
        qtd = self.quantidade
        if qtd == int(qtd) or qtd < 1:
            qtd = str(Fraction(qtd))
        else:
            parte_inteira = int(qtd)
            parte_fracionaria = qtd - parte_inteira
            parte_fracionaria = str(Fraction(parte_fracionaria))
            qtd = f'{parte_inteira} {parte_fracionaria}'
        de = ' de ' if self.quantificador!='' else ' '
        return f'{qtd} {self.quantificador}{de}{self.produto_ingrediente}'


class Receita(models.Model):
    nome = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    ingrediente_receita = models.ManyToManyField(Ingrediente)
    preparo = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    img = models.ImageField(blank=True)

    def __str__(self):
        return self.nome

