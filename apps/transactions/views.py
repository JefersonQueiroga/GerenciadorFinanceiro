from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from apps.transactions.models import *

from .forms import TransactionForm


class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = "transactions/transaction_form.html"
    success_url = reverse_lazy("transactions:list")

class TransactionListView(ListView):
    model = Transaction
    context_object_name=''
    queryset = Transaction.objects.all()
    paginate_by =4

class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class=TransactionForm
    success_url = reverse_lazy("transactions:list")

