from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

layout = """
    <h1> Sitio web con Django | Carlos Salinas C</h1>
    <hr/>
    <ul>
        <li>
        <a href="/inicio"> Inicio </a>
        </li>
        <li>
        <a href="/hola-mundo"> Hola mundo </a>
        </li>
        <li>
        <a href="/pagina-pruebas"> Página de pruebas </a>
        </li>
        <li>
        <a href="/contacto"> Contacto </a>
        </li>
    </ul>
    <hr/>
    """

nombre = "Carlos SC"
lenguajes = ["JavaScript", "Python", "PHP", "C#", "Java", "HTML"]

año = 2021
hasta = range(año, 2050)


def index(request):
    return render(request, 'index.html', {
        'mi_variable' : "Soy un dato que está en la vista",
        'title' : 'Inicio',
        'nombre' : nombre,
        'lenguajes' : lenguajes,
        'years' : hasta
        })

def hola_mundo(request):
    return render(request, 'hola_mundo.html')


def pagina(request, redirigir=0):

    if redirigir == 1:
        return redirect('contacto', nombre="Carlos", apellidos="SC")

    return render(request, 'pagina.html', {
        'texto' : "Aquí una wea random wkdjaskdj"
    })


def contacto(request, nombre="", apellidos=""):

    html = ""

    if nombre and apellidos:
        html += "<p>El nombre completo es: </p>"
        html += f"<h3> {nombre} {apellidos} </h3>"

    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)