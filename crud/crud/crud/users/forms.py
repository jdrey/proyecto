from django.forms import modelformset_factory
from django.forms import ModelForm

from users.models import Equipo


class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = "__all__"