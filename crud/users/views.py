from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404, JsonResponse
from users.models import Equipo
from users.forms import EquipoForm
from django.views import View

# MVC
def equipos(request):
    no_equipos = Equipo.objects.count()
    # products = Product.objects.all()
    equipos = Equipo.objects.order_by("id")
    return render(
        request,
        "equipos.html",
        {"no_equipos": no_equipos, "equipos": equipos},
    )

def nuevoEquipo(request):
    if request.method == "POST":
        formaEquipo = EquipoForm(request.POST)
        if formaEquipo.is_valid():
            formaEquipo.save()
            return redirect("equipos")

        else:
            return render(
                request, "nuevo-equipo.html", {"formaEquipo": formaEquipo}
            )
    else:
        formaEquipo = EquipoForm()

    return render(request, "nuevo-equipo.html", {"formaEquipo": formaEquipo})

def editarEquipo(request, id):
    try:
        equipo = get_object_or_404(Equipo, pk=id)

        if request.method == "POST":
            formaEquipo = EquipoForm(request.POST, instance=equipo)
            if formaEquipo.is_valid():
                formaEquipo.save()
                return redirect("equipos")

            else:
                return render(
                    request,
                    "editar-equipo.html",
                    {"formaEquipo": formaEquipo},
                )
        else:
            formaEquipo = EquipoForm(instance=equipo)

    except Equipo.DoesNotExist:
        raise Http404("El equipo no existe")

    return render(request, "editar-equipo.html", {"formaEquipo": formaEquipo})

def eliminarEquipo(request, id):

    try:
        equipo = get_object_or_404(Equipo, pk=id)
        if equipo:
            equipo.delete()

        return redirect("equipos")
    except Equipo.DoesNotExist:
        raise Http404("El equipo no existe")

# API

class EquiposView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        lista = Equipo.objects.all()
        return JsonResponse(list(lista.values()), safe=False)
    
    def post(self, request):
        data = json.loads(request.body)
        Equipo.objects.create(nombre=data['nombre'], ciudad=data['ciudad'], titulos=data['titulos'])
        datos = {'message': "Equipo creado"}
        return JsonResponse(datos)

    def put(self, request, id):
        data = json.loads(request.body)
        equipos = list(Equipo.objects.filter(id=id).values())
        if len(equipos) > 0:
            equipos = Equipo.objects.get(id=id)
            equipos.nombre = data['nombre']
            equipos.ciudad = data['ciudad']
            equipos.titulos = data['titulos']
            equipos.save()
            datos = {'message': "Equipo actualizado"}
        else:
            datos = {'message': "Equipo no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, id):
        equipos = list(Equipo.objects.filter(id=id).values())
        if len(equipos) > 0:
            Equipo.objects.filter(id=id).delete()
            datos = {'message': "Equipo eliminado"}
        else:
            datos = {'message': "Equipo no encontrado"}
        return JsonResponse(datos)



