
from django.db import models
from datetime import datetime


class Alumno(models.Model):
    dni_alumno = models.IntegerField()
    apellido_alumno = models.CharField(max_length=50)
    nombre_alumno = models.CharField(max_length=50)
    curso_alumno = models.ForeignKey('Curso', on_delete=models.CASCADE)
    docente_alumno = models.ForeignKey(
        'Docente', null=True, blank=True, on_delete=models.CASCADE)
    tutor = models.ForeignKey('Tutor', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __str__(self) -> str:
        return f'{self.apellido_alumno} {self.nombre_alumno}'


class Docente(models.Model):
    dni_docente = models.IntegerField()
    apellido_docente = models.CharField(max_length=50)
    nombre_docente = models.CharField(max_length=50)
    telefono_docente = models.IntegerField()

    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"

    def __str__(self):
        return f'{self.apellido_docente}, {self.nombre_docente}'

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=50)
    anio_lectivo = models.PositiveIntegerField(
        default=datetime.now().year, verbose_name='Año Lectivo')
    docente = models.ForeignKey('Docente', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return f'{self.nombre_curso} {self.anio_lectivo}'
    
class Tutor(models.Model):
    dni_tutor = models.IntegerField()
    apellido_tutor = models.CharField(max_length=50)
    nombre_tutor = models.CharField(max_length=50)
    telefono_tutor = models.IntegerField()

    class Meta:
        verbose_name = "Tutor"
        verbose_name_plural = "Tutores"

    def __str__(self):
        return f'{self.apellido_tutor} {self.nombre_tutor}'


class Direccion(models.Model):
    dni_tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    barrio = models.CharField(
        max_length=50, blank=True, null=True, default=None)
    vivienda = models.CharField(
        max_length=100, blank=True, null=True, default=None)
    calle = models.CharField(
        max_length=100, blank=True, null=True, default=None)
    casa = models.CharField(max_length=100, blank=True,
                            null=True, default=None)
    piso = models.CharField(max_length=50, blank=True, null=True, default=None)
    depto = models.CharField(
        max_length=100, blank=True, null=True, default=None)
    sector = models.CharField(
        max_length=50, blank=True, null=True, default=None)

    def __str__(self):
        return f'{self.dni_tutor}'
