from django.contrib import admin
from .models import HistoriaClinica, Paciente, Medico  # Importa tus modelos

admin.site.register(HistoriaClinica)  # Registra los modelos
admin.site.register(Paciente)
admin.site.register(Medico)
