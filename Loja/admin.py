from django.contrib import admin
from .models import Produto, Categoria, Usuario, Carrinho, Pedido

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'ano_lancamento', 'preco', 'quantidade_estoque', 'categorias')
    search_fields = ('titulo', 'descricao', 'categorias')
    list_filter = ('categorias',)
admin.site.register(Produto, ProdutoAdmin)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
admin.site.register(Categoria, CategoriaAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'senha', 'endereco', 'telefone', 'data_cadastro')
    search_fields = ('nome', 'email', 'endereco', 'telefone')
    list_filter = ('nome',)
admin.site.register(Usuario, UsuarioAdmin)

class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('quantidade', 'usuario', 'produto')
    search_fields = ('usuario', 'produto')
    list_filter = ('usuario',)
admin.site.register(Carrinho, CarrinhoAdmin)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('data_pedido', 'valor_total', 'metodo', 'usuario')
    search_fields = ('usuario', 'metodo')
    list_filter = ('usuario',)
admin.site.register(Pedido, PedidoAdmin)

# Register your models here.
