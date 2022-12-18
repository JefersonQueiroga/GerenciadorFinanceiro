from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from apps.transactions.models import Cliente

from .forms import ClienteForm, EnderecoFormSet


class AdicionarPessoaView(CreateView):
    def get(self, request, form, *args, **kwargs):
        self.object = None
        endereco_form = EnderecoFormSet(prefix="endereco_form")

        return self.render_to_response(
            self.get_context_data(
                form=form,
                endereco_form=endereco_form,
            )
        )


class ClienteCreateView(AdicionarPessoaView):
    model = Cliente
    template_name = "cadastro/pessoa_add.html"
    success_url = reverse_lazy("transactions:listaclientesview")
    success_message = "Cliente adicionado com sucesso."
    permission_codename = "add_cliente"

    def get(self, request, *args, **kwargs):
        form = ClienteForm(prefix="cliente_form")
        return super(ClienteCreateView, self).get(request, form, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super(ClienteCreateView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = ClienteForm(request.POST, prefix="cliente_form")
        endereco_form = EnderecoFormSet(request.POST, prefix="endereco_form")

        if form.is_valid() and endereco_form.is_valid():
            self.object = form.save(commit=False)
            self.object.created_by = self.request.user
            self.object.save()

            # Salvar informacoes endereco
            endereco_form.instance = self.object
            endereco_form.save()

            return self.form_valid(form)

        return self.form_invalid(form=form, endereco_form=endereco_form)


class ClienteListView(ListView):
    template_name = "cadastro/pessoa_list.html"
    model = Cliente
