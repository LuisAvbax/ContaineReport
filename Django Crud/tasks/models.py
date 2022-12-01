from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Crea una tabla de sql llamada Tasks
class Task(models.Model):
    # Titulo de la tarea
    title = models.CharField(max_length=100)
    # Descripcion de la tarea. Puede estar vacio
    description = models.TextField(blank=True)
    # Fecha en la que fue creada. Se añade la fecha y la hora por defecto sino se pasa el dato
    created = models.DateTimeField(auto_now_add=True)
    # Fecha en la que fue completada. Campo vacio inicialmente
    datecompleted = models.DateTimeField(null=True,blank=True)
    # Valor True o False si es importante. Si se crea una tarea esta marcada como NO importante
    important = models.BooleanField(default=False)
    # Usuario quien la creo. Cuando se elimina el usuario tambien se eliminaran las tareas relacionadas con ese usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title + '- by '+ self.user.username


""" python manage.py makemigrations
    python manage.py migrate """