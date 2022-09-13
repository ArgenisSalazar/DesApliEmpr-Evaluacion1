from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import math

# Create your views here.
@login_required
def index(request):
    return render(request, 'aplicacion/index.html')

def form_pago(request):
    return render(request, 'aplicacion/form_pago.html')

def mostrar_pago(request):
    nombre=request.POST.get('nombre')
    apellido=request.POST.get('apellido')
    num_hora=request.POST.get('num_hora')
    pago_hora=request.POST.get('pago_hora')
    if num_hora + '<=48':
        total = num_hora +'*'+ pago_hora+'+50'
        pago = eval(total)
    else:
        hora_ext=num_hora+'-48'
        pago=hora_ext+'*'+pago_hora+'+50+48*'+pago_hora

    context={
        'nombre':nombre,
        'apellido':apellido,
        'pago':pago,
    }

    return render(request, 'aplicacion/mostrar_pago.html', context)

def salir(request):
    logout(request)
    return redirect('/')