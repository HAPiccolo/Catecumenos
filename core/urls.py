from django.urls import path
from .views import home, consultas, registrar, supervisor, docentes, cursos, eliminar_curso, eliminar_docente, usuarios, asignacion_cursos



urlpatterns = [

path('', home, name='home'),
path('consultas/', consultas, name='consultas'),
path('registrar/', registrar, name='registrar'),
path('administrador/', supervisor, name='administrador'),
path('docentes/', docentes, name='docentes'),
path('cursos/', cursos, name='cursos'),
path('eliminar_curso/<int:curso_id>/', eliminar_curso, name='eliminar_curso'),
path('eliminar_docente/<int:docente_id>/', eliminar_docente, name='eliminar_docente'),
path('usuarios/', usuarios, name='usuarios'),
path('asignacion_cursos/', asignacion_cursos ,name='asignacion_cursos')

# Al cerrar sesion nos envia al home

]