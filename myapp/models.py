from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name

class Tasks(models.Model):  
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    done = models.BooleanField(default=False)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    usersesion=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.title + ' - ' + self.project.name   

#TextField para textos largos
#CharField para textos cortos

#Este campo project lo relacionamos con un project de verdad
    #Cuando tenemos tareas las relacionamos a un proyecto al que pertenece, por ende, utilizamos 
    #models.ForeignKey para relacionar nuestra variable project con la tabla Project donde tenemos los proyectos
    #Si eliminamos un proyecto, que pasa con la tarea? Le colocaremos una funcion para estos casos
    #on_delete = models.CASCADE
    #utilizamos coma , para separar la funcion on_delete de nuestra relacion
    #models.CASCADE eliminara los datos que tienen relacion con otro archivo eliminado en cascada