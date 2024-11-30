from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Produto, Categoria, Carrinho, ItemCarrinho, Pedido, Perfil

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'ano_lancamento', 'preco', 'quantidade_estoque', 'autores', 'elenco')
    search_fields = ('titulo', 'descricao')
   
admin.site.register(Produto, ProdutoAdmin)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
admin.site.register(Categoria, CategoriaAdmin)

class PerfilAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('endereco', 'telefone', 'data_cadastro')}),
    )
admin.site.register(Perfil, PerfilAdmin)

class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('quantidade', 'usuario', 'produto')
    search_fields = ('usuario', 'produto')
    list_filter = ('usuario',)
admin.site.register(Carrinho, CarrinhoAdmin)

class ItemCarrinhoAdmin(admin.ModelAdmin):
    list_display = ('carrinho','produto','quantidade')
    
admin.site.register( ItemCarrinho,ItemCarrinhoAdmin)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('data_pedido', 'valor_total', 'metodo_pagamento', 'usuario')
    search_fields = ('usuario', 'metodo')
    list_filter = ('usuario',)
admin.site.register(Pedido, PedidoAdmin)

# Register your models here.
