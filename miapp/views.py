from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Articulo
from miapp.models import Autor
from django.db.models import Q

# Create your views here.
layout = """
    <h1> Proyecto Web (LP3) || Flor Cerdán </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/saludo">Mensaje de Saludo</a>
        </li>
        <li>
            <a href="/rango">Mostrar Numeros [a,b]</a>
        </li>
        <li>
            <a href="/rango2">Mostrar Numeros [a,b] (Con Parámetro)</a>
        </li>
    </ul>
    <hr/>
"""


def index(request):
    estudiantes = [
        'SERGIO DANIEL VITE COCHACHIN',
        'ANTHONY GERARDO BENDEZU SANTISTEBAN',
        'CRISTIAN ALEXIS CHIPANA HUAMAN',
        'CARLOS GUSTAVO OYOLA SAAVEDRA',
        'GERARDO MANUEL CASTILLO TORDOYA'
    ]
    
    return render(request, 'index.html', {
        'titulo': 'Inicio',
        'mensaje': 'Proyecto Web con DJango',
        'estudiantes': estudiantes
    })


def saludo(request):
    return render(request, 'saludo.html', {
        'titulo': 'Saludo',
        'autor_saludo': 'Mg. Flor Elizabeth Cerdán León'
    })


def rango(request):
    a = 10
    b = 20
    rango_numeros = range(a,b+1)
    return render(request, 'rango.html',{
        'titulo': 'Rango',
        'a':a,
        'b':b,
        'rango_numeros':rango_numeros
    })


def rango2(request, a=0, b=100):
    if a > b:
        return redirect('rango2', a=b, b=a)

    resultado = f"""
        <h2> Rango con parámetros </h2>
        <h2> Número de [{a},{b}] </h2>
        Resultado: <br>
        <ul>
    """
    while a <= b:
        resultado += f"<li> {a} </li>"
        a += 1

    resultado += "</ul>"
    return HttpResponse(layout + resultado)

def crear_articulo(request, titulo, contenido, publicado):
    articulo = Articulo(
        titulo = titulo,
        contenido = contenido,
        publicado = publicado
    )
    articulo.save()
    return HttpResponse(f"Artículo Creado: {articulo.titulo} - {articulo.contenido}")

def buscar_articulo(request):
    try:
        articulo = Articulo.objects.get(id=2)
        resultado = f"""Articulo: 
                        <br> <strong>ID:</strong> {articulo.id} 
                        <br> <strong>Título:</strong> {articulo.titulo} 
                        <br> <strong>Contenido:</strong> {articulo.contenido}
                        """
    except:
        resultado = "<h1> Artículo No Encontrado </h1>"
    return HttpResponse(resultado)

def editar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)

    articulo.titulo = "Enseñanza onLine en la UNTELS"
    articulo.contenido = "Aula Virtual, Google Meet, Portal Académico, Google Classroom..."
    articulo.publicado = False

    articulo.save()
    return HttpResponse(f"Articulo Editado: {articulo.titulo} - {articulo.contenido}")

def listar_articulos(request):
    articulos = Articulo.objects.all()
    """
    articulos = Articulo.objects.filter(
        Q(titulo__contains="Py") |
        Q(titulo__contains="Hab")
    )
    """
    return render(request, 'listar_articulos.html',{
        'articulos': articulos,
        'titulo': 'Listado de Artículos'
    })

def eliminar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)
    articulo.delete()
    return redirect('listar_articulos')

def save_articulo(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        if len(titulo)<=5:
            return HttpResponse("<h2>El tamaño del título es pequeño, intente nuevamente</h2>")
        contenido = request.POST['contenido']
        publicado = request.POST['publicado']

        articulo = Articulo(
            titulo = titulo,
            contenido = contenido,
            publicado = publicado
        )
        articulo.save()
        return HttpResponse(f"Articulo Creado: {articulo.titulo} - {articulo.contenido}")
    else:
        return HttpResponse("<h2> No se ha podido registrar el artículo </h2>")

def create_articulo(request):
    return render(request, 'create_articulo.html')






def crear_autor(request, nombre):
    autor = Autor(
        autor = autor,
    )
    articulo.save()
    return HttpResponse(f"Autor Creado: {autor.nombre} - {autor.apellido}")

def buscar_autor(request):
    try:
        autor = Autor.objects.get(id=2)
        resultado = f"""Autor: 
                        <br> <strong>ID:</strong> {autor.id} 
                        <br> <strong>Nombre:</strong> {autor.nombre} 
                        <br> <strong>Apellido:</strong> {autor.apellido}
                        """
    except:
        resultado = "<h1> Autor No Encontrado </h1>"
    return HttpResponse(resultado)

def editar_autor(request, id):
    autor = Autor.objects.get(pk=id)

    autor.nombre = "XXXXXXXXXXXXXXXXXX"


    autor.save()
    return HttpResponse(f"Autor Editado: {autor.nombre}")

def listar_autores(request):
    autores = Autor.objects.all()
    """
    autores = Autor.objects.filter(
        Q(titulo__contains="Py") |
        Q(titulo__contains="Hab")
    )
    """
    return render(request, 'listar_autores.html',{
        'autores': autores,
        'nombre': 'Listado de Autores'
    })

def eliminar_autor(request, id):
    autor = autor.objects.get(pk=id)
    autor.delete()
    return redirect('listar_autores')

def save_autor(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        if len(nombre)<=0:
            return HttpResponse("<h2>No ha ingresado nombre de autor, intente nuevamente</h2>")
        apellido = request.POST['apellido']
        sexo = request.POST['sexo']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        pais = request.POST['pais']

        autor = Autor(
            nombre = nombre,
            apellido = apellido,
            sexo = sexo,
            fecha_nacimiento = fecha_nacimiento,
            pais = pais,
        )
        autor.save()
        return HttpResponse(f"Autor Creado: {autor.nombre}")
    else:
        return HttpResponse("<h2> No se ha podido registrar el autor </h2>")

def create_autor(request):
    return render(request, 'create_autor.html')