from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from apps.transactions.models import *

from .forms import TransactionForm
from .filter import TransactionsFilter


class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = "transactions/transaction_form.html"
    success_url = reverse_lazy("transactions:list")


class TransactionListView(ListView):
    model = Transaction
    queryset = Transaction.objects.all()
    paginate_by = 4
    filterset_class = TransactionsFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form
        return context


class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy("transactions:list")
