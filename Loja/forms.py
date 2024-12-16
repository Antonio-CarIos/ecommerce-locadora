import django.forms as forms
from .models import Produto, Perfil
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['titulo', 'descricao', 'ano_lancamento', 'preco','quantidade_estoque','categorias','imagem','autores','elenco']
        widgets =  {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'ano_lancamento': forms.NumberInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantidade_estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            'categorias': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'autores': forms.TextInput(attrs={'class': 'form-control'}),
            'elenco': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PerfilCreationForm(UserCreationForm):
    class Meta:
        model = Perfil
        fields = ['first_name','last_name','username','email','endereco','telefone','password1','password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'placeholder': 'Nome'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Sobrenome'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Nome de usuário'})
        self.fields['email'].widget.attrs.update({'placeholder': 'E-mail'})
        self.fields['endereco'].widget.attrs.update({'placeholder': 'Endereço'})
        self.fields['telefone'].widget.attrs.update({'placeholder': 'Telefone'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Senha'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirme sua senha'})
        
        