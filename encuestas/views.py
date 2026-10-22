from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, QueryDict

# from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from utils import limpiar_texto

import json

from .models import Profesor

# Create your views here.


def get(request):
    # return HttpResponse("<h1>¡Hola! Esta es la página principal de Encuestas.</h1>")
    hola = " m a l o"
    # texto = limpiar_texto(hola)

    # return HttpResponse(texto.encode("utf-8"), content_type="text/plain")
    return render(request, "home.html", {"text": limpiar_texto(hola)})


@login_required
def home_view(request):
    # Puedes pasarle el usuario actual a la plantilla para saludarlo
    contexto = {"usuario": request.user}
    return render(request, "home.html", contexto)


def logout_view(request):
    logout(request)
    return redirect("login")


# CRUD
@csrf_exempt
def profesor_view(request):
    print("-.--->", request.method)
    if request.method == "POST":
        print("Profesor......", request.POST)
        nombre = request.POST.get("nombre")
        especialidad = request.POST.get("especialidad")

        print(nombre, especialidad)
        profesor = Profesor.objects.create(nombre=nombre, especialidad=especialidad)
        print("Profesor creado:", profesor)

        return JsonResponse({"status": "ok", "profesor_name": profesor.nombre})

    if request.method == "PUT":
        put_data = QueryDict(request.body)
        nombre = put_data.get("nombre")
        especialidad = put_data.get("especialidad")
        print("paso al put", nombre, especialidad)
        # Aquí podrías manejar la actualización de un profesor
        profesor = Profesor.objects.filter(nombre=nombre).first()
        print("---", profesor)
        if profesor:
            profesor.especialidad = especialidad
            profesor.save()
            return JsonResponse({"status": "ok", "message": "Profesor actualizado"})
        else:
            return JsonResponse(
                {"status": "error", "message": "Profesor no encontrado"}
            )
    if request.method == "GET":
        print(request.GET)
        profesor = Profesor.objects.filter(nombre=request.GET.get("nombre"))
        print(profesor)
        data = []
        for p in profesor:
            data.append({"nombre": p.nombre, "especialidad": p.especialidad})
        return JsonResponse({"status": "ok", "message": data})

@csrf_exempt
def musico1(request):
    if request.method == "POST":
        print("Musio......", request.POST)
        nombre = request.POST.get("first_name")
        especialidad = request.POST.get("last_name")
        .......


def login_view(request):
    if request.method == "POST":
        print(request.POST)
        # 1. Obtener los datos enviados desde el formulario HTML
        usuario_input = request.POST.get("username")
        password_input = request.POST.get("password")

        # 2. Autenticar el usuario contra la base de datos
        user = authenticate(request, username=usuario_input, password=password_input)

        if user is not None:
            # 3. Si las credenciales son correctas, se crea la sesión
            login(request, user)
            return redirect("home")  # Redirige a la página principal
        else:
            # 4. Si es incorrecto, vuelve a mostrar el login con un mensaje
            return render(
                request, "login.html", {"error": "Usuario o contraseña incorrectos"}
            )

    # Si la petición es GET (cargar la página por primera vez)
    return render(request, "login.html")
