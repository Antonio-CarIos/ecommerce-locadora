from django.db import models
from django.contrib.auth.models import AbstractUser

class Perfil(AbstractUser):
    email = models.EmailField()
    endereco = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_cadastro = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.username

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ano_lancamento = models.IntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade_estoque = models.IntegerField()
    categorias = models.ManyToManyField(Categoria)
    imagem = models.ImageField(upload_to='capas-filmes/')
    autores = models.TextField()
    elenco = models.TextField()

    def __str__(self):
        return self.titulo

class Carrinho(models.Model):
    usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrinho de {self.usuario.username}"

    def total_itens(self):
        return sum(item.quantidade for item in self.itens.all())

    def total_preco(self):
        return sum(item.total_preco for item in self.itens.all())
      
class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.titulo} no {self.carrinho}"

    @property
    def total_preco(self):
        return self.quantidade * self.produto.preco

class Pedido(models.Model):
    usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    data_pedido = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)
    metodo_pagamento = models.CharField(max_length=50, choices=[
        ('Pix', 'Pix'),
        ('Cartão de Crédito', 'Cartão de Crédito'),
        ('Dinheiro Físico', 'Dinheiro Físico')
    ])
   
    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"
    