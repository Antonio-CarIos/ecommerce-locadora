from django.db import models
  
class Produto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ano_lancamento = models.IntegerField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade_estoque = models.IntegerField()
    categorias = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='capas-filmes/')
    autores = models.TextField()
    elenco = models.TextField()


    def __str__(self):
        return self.titulo
    
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    produtos = models.ManyToManyField(Produto)

    def __str__(self):
        return self.nome   
     
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    data_cadastro = models.DateField()


    def __str__(self):
        return self.nome
    

class Carrinho(models.Model):
    quantidade = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.produto.titulo
    
class Pedido(models.Model):
    data_pedido = models.DateField()
    valor_total = models.DecimalField(max_digits=5, decimal_places=2)
    metodo= models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.nome
    

  







# Create your models here.
