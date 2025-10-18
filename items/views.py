# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ObjetoPerdido
from .forms import ComentarioForm, ObjetoForm

def index(request):
    return HttpResponse("<h1>¡Hola mundo! Primer Programa.</h1>")



def lista_objetos(request):
    objetos = ObjetoPerdido.objects.all().order_by('-fecha_publicacion')
    return render(request, 'items/lista.html', {'objetos': objetos})

def detalle_objeto(request, pk):
    objeto = get_object_or_404(ObjetoPerdido, pk=pk)
    return render(request, 'items/detalle.html', {'objeto': objeto})

@login_required
def crear_objeto(request):
    if request.method == 'POST':
        form = ObjetoForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.usuario = request.user
            objeto.save()
            return redirect('lista_objetos')
    else:
        form = ObjetoForm()
    return render(request, 'items/form.html', {'form': form})

@login_required
def editar_objeto(request, pk):
    objeto = get_object_or_404(ObjetoPerdido, pk=pk)
    if objeto.usuario != request.user and not request.user.is_staff:
        return redirect('lista_objetos')
    form = ObjetoForm(request.POST or None, instance=objeto)
    if form.is_valid():
        form.save()
        return redirect('lista_objetos')
    return render(request, 'items/form.html', {'form': form})

@login_required
def eliminar_objeto(request, pk):
    objeto = get_object_or_404(ObjetoPerdido, pk=pk)
    if objeto.usuario == request.user or request.user.is_staff:
        objeto.delete()
    return redirect('lista_objetos')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_objetos')
    else:
        form = UserCreationForm()
    return render(request, 'items/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lista_objetos')
    else:
        form = AuthenticationForm()
    return render(request, 'items/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('lista_objetos')

def detalle_objeto(request, pk):
    objeto = get_object_or_404(ObjetoPerdido, pk=pk)
    comentarios = objeto.comentarios.all().order_by('-fecha')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.objeto = objeto
                comentario.usuario = request.user
                comentario.save()
                return redirect('detalle_objeto', pk=pk)
        else:
            return redirect('login')
    else:
        form = ComentarioForm()

    return render(request, 'items/detalle.html', {
        'objeto': objeto,
        'comentarios': comentarios,
        'form_comentario': form
    })
