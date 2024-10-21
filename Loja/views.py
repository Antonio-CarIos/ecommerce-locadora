from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm

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