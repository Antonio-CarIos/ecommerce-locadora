import django.forms as forms
from .models import Produto


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
            'categorias': forms.TextInput(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'autores': forms.TextInput(attrs={'class': 'form-control'}),
            'elenco': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        