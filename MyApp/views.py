from django.shortcuts import render, redirect
from .models import Tarea
from .form  import TareaForm
from django.http import HttpResponse



def tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tarea/index.html', {'tareas': tareas})


def crear(request):
    formulario = TareaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('tareas')
    return render(request, 'tarea/crear.html', {'formulario':formulario} )

def completar(request, id):
    tarea = Tarea.objects.get(id=id)
    tarea.completada = True
    tarea.save()
    return redirect('tareas')


def editar(request, id):
    tarea = Tarea.objects.get(id=id)
    formulario = TareaForm(request.POST or None, request.FILES or None, instance=tarea)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('tareas')
    return render(request, 'tarea/editar.html', {'formulario': formulario})

def eliminar(request, id):
    tarea = Tarea.objects.get(id=id)
    tarea.delete()
    return redirect('tareas')