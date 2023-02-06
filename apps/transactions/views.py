from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from apps.transactions.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TransactionForm
from .filter import TransactionsFilter
from rolepermissions.mixins import HasRoleMixin


class TransactionCreateView(HasRoleMixin, LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = "transactions/transaction_form.html"
    success_url = reverse_lazy("transactions:list_transaction")
    allowed_roles = "administrador"


class TransactionListView(HasRoleMixin, LoginRequiredMixin, ListView):
    model = Transaction
    queryset = Transaction.objects.all()
    paginate_by = 4
    filterset_class = TransactionsFilter
    allowed_roles = ["funcionario", "administrador"]

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form

        return context


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy("transactions:list")
