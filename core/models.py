
from django.db import models


class Alumno(models.Model):
    dni_alumno = models.IntegerField(primary_key=True)
    apellido_alumno = models.CharField(max_length=50)
    nombre_alumno = models.CharField(max_length=50)
    curso_alumno = models.ForeignKey('Curso', on_delete=models.CASCADE)
    docente_alumno = models.ForeignKey(
        'Docente', null=True, blank=True, on_delete=models.CASCADE)
    tutor = models.ForeignKey('Tutor', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.apellido_alumno} {self.nombre_alumno}'


class Curso(models.Model):
    nombre_curso = models.CharField(max_length=50)
    docente = models.ForeignKey('Docente', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.nombre_curso}'


class Docente(models.Model):
    dni_docente = models.IntegerField(primary_key=True)
    apellido_docente = models.CharField(max_length=50)
    nombre_docente = models.CharField(max_length=50)
    telefono_docente = models.IntegerField()

    

    def __str__(self):
        return f'{self.apellido_docente}, {self.nombre_docente}'


class Tutor(models.Model):
    dni_tutor = models.IntegerField(primary_key=True)
    apellido_tutor = models.CharField(max_length=50)
    nombre_tutor = models.CharField(max_length=50)
    telefono_tutor = models.IntegerField()

    def __str__(self):
        return f'{self.apellido_tutor} {self.nombre_tutor}'
