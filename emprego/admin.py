from django.contrib import admin
from .models import Usuario, Empresa, Candidato

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Empresa)
admin.site.register(Candidato)

