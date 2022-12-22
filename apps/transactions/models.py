from django.conf import LazySettings
from django.db import DatabaseError, models
from apps.core.models import BaseModel
from .constants import TYPE_TRANSACTION

# Create your models here.


class FormPayment(BaseModel):
    name = models.CharField("Nome", max_length=70)
    active = models.BooleanField()

    class Meta:
        verbose_name = "Forma de Pagamento"
        verbose_name_plural = "Formas de Pagamento"

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class Transaction(BaseModel):

    description = models.CharField(max_length=200)
    type_operation = models.CharField(
        max_length=10, choices=TYPE_TRANSACTION, verbose_name="Categoria"
    )
    form_payment = models.ForeignKey(
        FormPayment, on_delete=models.SET_NULL, null=True, blank=True
    )
    category = models.ForeignKey(Category, on_delete=models.ForeignKey)
    date_transaction = models.DateField(verbose_name="Data da Transação")

    class Meta:
        verbose_name = "Transação"
        verbose_name_plural = "Transações"

    def __str__(self):
        return self.description
