from django.shortcuts import render, HttpResponse
from .models import Alumno, Tutor, Curso, Docente
from django.contrib import messages
from .exceptions import AlumnoExistException
# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def consultas(request):
    alumno = None
    tutor = None
    docente = None

    if request.method == "POST":
        dni_alumno = request.POST.get("dni_alumno", None)  # Obtiene el DNI ingresado por el usuario

        if dni_alumno:
            try:
                # Realiza la consulta para obtener el alumno y su tutor
                alumno = Alumno.objects.get(dni_alumno=dni_alumno)
                tutor = alumno.tutor  # Supongamos que tienes una relación ForeignKey en tu modelo Alumno
                # También puedes obtener el docente asociado al alumno según tu modelo de datos
                docente = alumno.docente_alumno  # Supongamos que el curso tiene un campo ForeignKey al docente
                return render(request, 'core/consultas.html', {'alumno': alumno, 'tutor': tutor, 'docente': docente})
            except Alumno.DoesNotExist:
                error_message = "No se encontró ningún alumno con el DNI proporcionado."

    return render(request, 'core/consultas.html')


def registrar(request):

    if request.method == "POST":
        dni_alumno = request.POST["dni_alumno"]
        apellido_alumno = request.POST["apellido_alumno"]
        nombre_alumno = request.POST["nombre_alumno"]
        cursoid = request.POST["curso"]

        nombre_curso = Curso.objects.get(id=cursoid)

        dni_tutor = request.POST["dni_tutor"]
        apellido_tutor = request.POST["apellido_tutor"]
        nombre_tutor = request.POST["nombre_tutor"]
        telefono_tutor = request.POST["telefono_tutor"]

        try:
            # Busca un tutor existente o crea uno nuevo
            tutor, created = Tutor.objects.get_or_create(
                dni_tutor=dni_tutor,
                defaults={'apellido_tutor': apellido_tutor,
                          'nombre_tutor': nombre_tutor, 'telefono_tutor': telefono_tutor}
            )
            if not created:
                raise AlumnoExistException(
                    "El alumno ya existe. No se puede crear el registro porque tiene el mismo DNI.")

            alumno = Alumno.objects.create(dni_alumno=dni_alumno, apellido_alumno=apellido_alumno,
                                           nombre_alumno=nombre_alumno, curso_alumno=nombre_curso, tutor=tutor)

            alumno.save()

            return render(request, 'core/sucess_save.html')

        except AlumnoExistException as e:
            # Muestra mensaje de error al usuario
            messages.error(request, str(e))
            return render(request, 'core/error_save.html')

    else:
        # Trae todo el objeto
        cursos = Curso.objects.all()
        docentes = Docente.objects.all()

        datos = {
            'cursos': cursos,
            'docentes': docentes,
        }
        return render(request, 'core/registrar.html', datos)
