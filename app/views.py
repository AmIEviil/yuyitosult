from email import message
from django.shortcuts import render
from django.db import connection
from .models import *
# Create your views here.
import base64
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect

from app.carrito import Carrito

def vista_prod(request,id):
    id_tipo = TipoProducto.objects.get(id_tipo_producto=id)
    productos = Producto.objects.filter(id_tipo_producto=id_tipo)
    contexto = {"productos":productos}
    print(productos)
    return render(request, 'app/vista_prod.html',contexto)

def visualizar_prod(request,id):
    producto = Producto.objects.get(id_producto=id)
    contexto = {"producto":producto}
    return render(request, 'app/producto.html',contexto)

def catalogo (request):

    datos_tipos = listado_Tipo_Productos()

    arreglo = []

    for i in datos_tipos:
        data = {
            'data':i,
            'img_tipo':str(base64.b64encode(i[2].read()), 'utf-8')
        }
        arreglo.append(data)
    data = {
        'categorias': arreglo,
    }

    return render(request, 'app/catalogo.html', data)

def productos(request):

    datos_tipos = listado_Productos()

    arreglo = []

    for i in datos_tipos:
        data = {
            'data':i,
            'img_producto':str(base64.b64encode(i[10].read()), 'utf-8')
        }
        arreglo.append(data)
    data = {
        'productos': listado_Productos(),
        'productos': arreglo,
    }

    return render(request, 'app/productos.html', data)

def agregar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=id_producto)
    carrito.agregar(producto)

    return redirect("carritodecompras")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carritodecompras")

def restar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=id_producto)
    carrito.restar(producto)
    return redirect("carritodecompras")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carritodecompras")

def quienessomos(request):
    return render(request, 'app/quienessomos.html')

def delivery(request):
    return render(request, 'app/delivery.html')

def busqueda(request):
    return render(request, 'app/busqueda.html')

def carritodecompras(request):
    return render(request, 'app/carritodecompras.html')

def fiado(request):
    return render(request, 'app/fiado.html')

def home(request):
    return render(request, 'app/home.html')

def mediosdepago(request):
    return render(request, 'app/mediosdepago.html')

def webpay(request):
    return render(request, 'app/webpay.html')

def pagowebpay(request):
    return render (request,'app/pagowebpay.html')

def bancos(request):
    return render(request, 'app/bancos.html')

def listado_Productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PRODUCTOS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

def listado_Tipo_Productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_TIPO_PRODUCTOS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario
    return render(request,'registration/registro.html',data)