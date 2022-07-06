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
    
    datos_tipos = buscar_Tipo_Productos(id)

    arreglo = []

    for i in datos_tipos:
        data = {
            'data':i,
            'img_producto':str(base64.b64encode(i[10].read()), 'utf-8')
        }
        arreglo.append(data)
    data = {
        'productos': arreglo,
    }

    return render(request, 'app/vista_prod.html',data)

def visualizar_prod(request,id):

    datos_tipos = buscar_Productos(id)

    arreglo = []

    for i in datos_tipos:
        data = {
            'data':i,
            'img_producto':str(base64.b64encode(i[10].read()), 'utf-8')
        }
        arreglo.append(data)
    data = {
        'productos': arreglo,
    }

    return render(request, 'app/producto.html', data)

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
    #'productos': listado_Productos(),
    #'productos': arreglo,
    data = {
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

def filtrar_palabra_clave(request):
    if request.POST:
        texto=request.POST.get("txtFiltrar")
        producto = Producto.objects.filter(nombre__contains=texto)

    data = {
        "producto":producto
    }
    print(texto)
    return render(request, "app/busqueda.html",data)

def listar_Producto(texto):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PRODUCTO", [texto,out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

def buscar_Productos(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_BUSCAR_PRODUCTOS", [id,out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

def buscar_Tipo_Productos(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_BUSCAR_TIPO_PRODUCTOS", [id,out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

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