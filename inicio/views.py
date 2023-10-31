from django.shortcuts import render, redirect
from inicio.models import Remera, Gorra, Zapatilla

def inicio(request):
    
    return render(request, 'inicio/inicio.html', {})

def remeras(request):
    
    marca_a_buscar = request.GET.get('marca')
    
    if marca_a_buscar:
        listado_remeras = Remera.objects.filter(marca__icontains=marca_a_buscar)
    else:
        listado_remeras = Remera.objects.all()
    
    return render(request, 'inicio/remeras.html', {'listado_remeras': listado_remeras})

def zapas(request):
    
    listado_zapas = Zapatilla.objects.all()
    
    return render(request, 'inicio/zapas.html', {'listado_zapas': listado_zapas})

def gorras(request):
    
    listado_gorras = Gorra.objects.all()
    
    return render(request, 'inicio/gorras.html', {'listado_gorras': listado_gorras})

def crear_remera(request):
    
    if request.method == 'POST':
        marca = request.POST.get('marca')
        descripcion = request.POST.get('descripcion')
        stock = request.POST.get('stock')
        
        remera = Remera(marca=marca, descripcion=descripcion,stock=stock)
        remera.save()

        return redirect('remeras')
    return render(request, 'inicio/crear_remera.html', {})

def crear_zapatillas(request):
    
    if request.method == 'POST':
        marca = request.POST.get('marca')
        color = request.POST.get('color')
        modelo = request.POST.get('modelo')
        stock = request.POST.get('stock')
        
        zapatilla = Zapatilla(marca=marca, color=color, modelo=modelo, stock=stock)
        zapatilla.save()

        return redirect('zapas')
    return render(request, 'inicio/crear_zapatillas.html', {})

def crear_gorra(request):
    
    if request.method == 'POST':
        marca = request.POST.get('marca')
        descripcion = request.POST.get('descripcion')
        stock = request.POST.get('stock')
        
        gorra = Gorra(marca=marca, descripcion=descripcion,stock=stock)
        gorra.save()

        return redirect('gorras')
        
    return render(request, 'inicio/crear_gorra.html', {})
