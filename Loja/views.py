from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Perfil
from .forms import ProdutoForm
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    produtos = Produto.objects.all()
    
    context = {
        'produtos' : produtos
    }
    
    return render (
        request,
        'index.html',
        context
    )

def detalhes(request, id):
    
    produto = get_object_or_404(Produto, id=id)

    context = {
        
        'produto' : produto
    }

    return render (
        request,
        'detalhe.html',
        context
    )

def registrar_usuario(request):
   


    return render (
        request,
        'registrar.html',

    )

def cadastrar_dvd(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProdutoForm()

    context = {
        'form': form
    }

    return render(
        request,
        'cadastrar.html',
        context
    )
    

def deletado(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('dashboard')

    context = {
        'produto': produto
    }

    return render(
        request,
        'deletar.html',
        context
    )

def editado(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProdutoForm(instance=produto)

    context = {
        'form': form,
        'produto': produto
    }

    return render(
        request,
        'editar.html',
        context
    )
    
def dashboards(request):
    produtos = Produto.objects.all()

    context = {
        'produtos':produtos
    }


    return render (
        request,
        'dashboard.html',
        context
    )

def lista_produtos(request):
    categoria = request.GET.get('category')
    preco_min = request.GET.get('price_min')
    preco_max = request.GET.get('price_max')
    ordenar = request.GET.get('sort')

    produtos_lista = Produto.objects.all().order_by('titulo')

    # Filtro por categoria
    if categoria:
        produtos_lista = produtos_lista.filter(categorias__nome=categoria)  # Ajuste aqui!

    # Filtro por faixa de preço
    if preco_min:
        produtos_lista = produtos_lista.filter(preco__gte=preco_min)
    if preco_max:
        produtos_lista = produtos_lista.filter(preco__lte=preco_max)

    # Ordenação
    if ordenar == 'price_asc':
        produtos_lista = produtos_lista.order_by('preco')
    elif ordenar == 'price_desc':
        produtos_lista = produtos_lista.order_by('-preco')
    else:
        produtos_lista = produtos_lista.order_by('titulo')


    paginator = Paginator(produtos_lista, 5)
    page = request.GET.get('page', 1)
    try :
        produtos = paginator.page(page)
    except:
        produtos = paginator.page(1)

    context = {
        'produtos':produtos,
        'categoria_selecionada': categoria,
        'preco_min': preco_min,
        'preco_max': preco_max,
        'ordenar': ordenar

    }

    return render (
        request,
        'catalogo.html',
        context
    )



