from django.urls import path
from .views import EquiposView

urlpatterns = [
    path("equipos/", EquiposView.as_view(), name="equiposList"),
    path('equipos/<int:id>', EquiposView.as_view(), name='equiposCrud')
]