from django.conf import LazySettings
from django.db import DatabaseError, models

from apps.core.models import BaseModel

# Create your models here.


class Cliente(BaseModel):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_nascimento = models.DateField()


class Endereco(BaseModel):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=150)


class FormaPagamento(BaseModel):
    nome = models.CharField(max_length=70)
    ativo = models.BooleanField()


class Transacao(BaseModel):
    class TipoOperacao(models.TextChoices):
        RECEITA = "RECEITA", ("Receita")
        DESPESA = "DESPESA", ("Despesa")

    descricao = models.CharField(max_length=200)
    tipo_categoria = models.CharField(
        max_length=10, choices=TipoOperacao.choices, verbose_name="Tipo Categoria"
    )
    forma_pagamento = models.ForeignKey(
        FormaPagamento, on_delete=models.SET_NULL, null=True, blank=True
    )
