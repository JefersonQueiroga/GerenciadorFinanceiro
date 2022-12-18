from django.forms import ModelForm, inlineformset_factory

from apps.transactions.models import Cliente, Endereco


class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = ["logradouro"]


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome", "email", "data_nascimento"]


EnderecoFormSet = inlineformset_factory(
    Cliente, Endereco, form=EnderecoForm, extra=1, can_delete=True
)
