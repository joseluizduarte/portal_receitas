from django.db import models
from django.db.models.fields import TextField


class Tag(models.Model):
    nome = models.CharField(max_length=50)

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
        return f'{self.quantidade} {self.quantificador} de {self.produto_ingrediente}'


class Receita(models.Model):
    nome = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    ingrediente_receita = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.nome


class Preparo(models.Model):
    ordem = models.IntegerField()
    instrucao = models.TextField()
    receita_preparo = models.ForeignKey(Receita, on_delete=models.PROTECT)

    def __str__(self):
        return self.instrucao