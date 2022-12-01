from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    # Cuales campos solo son de lectura y que se vean en la pantalla
    readonly_fields = ("created",)

# Register your models here.
admin.site.register(Task, TaskAdmin)