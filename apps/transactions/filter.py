from django_filters import FilterSet, ChoiceFilter, CharFilter
from django import forms
from .models import Transaction
from .constants import TYPE_TRANSACTION


class TransactionsFilter(FilterSet):
    description = CharFilter(
        lookup_expr="icontains", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    type_operation = ChoiceFilter(
        choices=TYPE_TRANSACTION, widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Transaction
        fields = ["description", "type_operation"]
