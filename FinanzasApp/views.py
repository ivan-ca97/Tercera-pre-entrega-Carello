from django.shortcuts import render

from django.urls import reverse_lazy
#==========|Class based views==========
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
#==========Class based views|==========

from .models import *

# Create your views here.

def homeFinanzas(request):
    return render(request, 'FinanzasApp\\home.html')



#====================|Persona====================#
class PersonaList(ListView):
    model = Persona

class PersonaCreate(CreateView):
    model = Persona
    fields = ['nombre', 'apellido', 'dni', 'email']
    success_url = reverse_lazy('personas')

class PersonaUpdate(UpdateView):
    model = Persona
    fields = ['nombre', 'apellido', 'dni', 'email']
    success_url = reverse_lazy('personas')

class PersonaDelete(DeleteView):
    model = Persona
    success_url = reverse_lazy('personas')
#====================Persona|====================#
    

#====================|Formas de pago====================#
class FormaDePagoList(ListView):
    model = FormaDePago

class FormaDePagoCreate(CreateView):
    model = FormaDePago
    fields = ['nombre', 'credito', 'descripcion']
    success_url = reverse_lazy('formas_de_pago')

class FormaDePagoUpdate(UpdateView):
    model = FormaDePago
    fields = ['nombre', 'credito', 'descripcion']
    success_url = reverse_lazy('formas_de_pago')

class FormaDePagoDelete(DeleteView):
    model = FormaDePago
    success_url = reverse_lazy('formas_de_pago')
#====================Formas de pago|====================#

#====================|Ingresos====================#
class IngresoList(ListView):
    model = Ingreso

class IngresoCreate(CreateView):
    model = Ingreso
    fields = ['nombreIngreso', 'descripcion', 'monto', 'titularNombre', 'fecha']
    success_url = reverse_lazy('ingresos')

class IngresoUpdate(UpdateView):
    model = Ingreso
    fields = ['nombreIngreso', 'descripcion', 'monto', 'titularNombre', 'fecha']
    success_url = reverse_lazy('ingresos')

class IngresoDelete(DeleteView):
    model = Ingreso
    success_url = reverse_lazy('ingresos')
#====================Ingresos|====================#
    
#====================|Egresos====================#
class EgresoList(ListView):
    model = Egreso

class EgresoCreate(CreateView):
    model = Egreso
    fields = ['nombreEgreso', 'descripcion', 'monto', 'titularNombre', 'formaDePago', 'fecha']
    success_url = reverse_lazy('egresos')

class EgresoUpdate(UpdateView):
    model = Egreso
    fields = ['nombreEgreso', 'descripcion', 'monto', 'titularNombre', 'formaDePago', 'fecha']
    success_url = reverse_lazy('egresos')

class EgresoDelete(DeleteView):
    model = Egreso
    success_url = reverse_lazy('egresos')
#====================Egresos|====================#
    

#====================|Busqueda====================#
def encontrarIngresosPorTitular(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        ingresos = Ingreso.objects.filter(titularNombre__icontains=patron)
        contexto = {"ingreso_list": ingresos}
        return render(request, "FinanzasApp/ingreso_list.html", contexto)
    else:
        ingresos = Ingreso.objects.all()
        contexto = {"ingreso_list": ingresos}
        return render(request, "FinanzasApp/ingreso_list.html", contexto)

def encontrarEgresosPorTitular(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        egresos = Egreso.objects.filter(titularNombre__icontains=patron)
        contexto = {"egreso_list": egresos}
        return render(request, "FinanzasApp/egreso_list.html", contexto)
    else:
        egresos = Egreso.objects.all()
        contexto = {"egreso_list": egresos}
        return render(request, "FinanzasApp/egreso_list.html", contexto)

#====================Busqueda|====================#
'''    
class EstudianteCreate(CreateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('estudiantes')

class EstudianteUpdate(UpdateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('estudiantes')

class EstudianteDelete(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiantes')
'''