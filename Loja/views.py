from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Perfil, Carrinho, ItemCarrinho
from .forms import ProdutoForm, PerfilCreationForm
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def home(request):
    produtos = Produto.objects.all().order_by('titulo')
    query = request.GET.get('search')  
    if query:
        produtos = Produto.objects.filter(titulo__icontains=query).order_by('titulo')  
    else:
        produtos = Produto.objects.all().order_by('titulo')  



    context = {
        'produtos' : produtos,
        'search_query': query
    }
    
    return render (request,'index.html',context)


def detalhes(request, id): 
    produto = get_object_or_404(Produto, id=id)

    context = {    
        'produto' : produto
    }

    return render (request,'detalhe.html',context)

def sobre(request):
    return render (request,'sobre.html')


def lista_produtos(request):
    categoria = request.GET.get('category')
    preco_min = request.GET.get('price_min')
    preco_max = request.GET.get('price_max')
    ordenar = request.GET.get('sort')

    produtos_lista = Produto.objects.all().order_by('titulo')

    # Filtro por categoria
    if categoria:
        produtos_lista = produtos_lista.filter(categorias__nome=categoria)  

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

    return render (request,'catalogo.html',context)



def registrar_usuario(request):
    if request.method == 'POST':
        form = PerfilCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            form.save()
            return redirect('home')
    else:
        form = PerfilCreationForm()

    return render (
        request,
        'registrar.html',
        {'form':form}
    )


def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'Usuário ou senha invalidos'})
    
    return render(request, 'login.html')


@login_required
def logout_usuario(request):
    logout(request)
    return redirect('home')


def admin_verificado(user):
    return user.is_staff


@user_passes_test(admin_verificado)
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


@user_passes_test(admin_verificado)
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

    return render(request,'cadastrar.html',context)


@user_passes_test(admin_verificado)
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

    return render(request,'editar.html',context)


@user_passes_test(admin_verificado)
def deletado(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('dashboard')

    context = {
        'produto': produto
    }

    return render(request,'deletar.html',context)

@login_required
def adicionar_ao_carrinho(request, id):
    produto = get_object_or_404(Produto, id=id)
    carrinho, criado = Carrinho.objects.get_or_create(usuario=request.user)

    item, criado = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
    if not criado:
        item.quantidade += 1
        item.save()

    return redirect('carrinho')

@login_required
def carrinho(request):
    carrinho, criado = Carrinho.objects.get_or_create(usuario=request.user)
    itens = carrinho.itens.select_related('produto')  
    total_preco = sum(item.total_preco for item in itens)
    total_itens = sum(item.quantidade for item in itens)

    context = {
        'carrinho': {
            'total_preco': total_preco,
            'total_itens': total_itens,
        },
        'itens': itens,
    }

    return render(request, 'carrinho.html', context)

def remover_item_carrinho(request, item_id):
    if request.user.is_authenticated:
        item = get_object_or_404(ItemCarrinho, id=item_id, carrinho__usuario=request.user)
        item.delete()  
    return redirect('carrinho')  