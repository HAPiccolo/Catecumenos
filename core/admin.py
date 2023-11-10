from django.contrib import admin
from .models import Alumno, Tutor, Docente, Curso
# Register your models here.

admin.site.register(Alumno)
admin.site.register(Tutor)
admin.site.register(Docente)
admin.site.register(Curso)
