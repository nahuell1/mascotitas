import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ubicacion = models.CharField(max_length=255, blank=True)
    numero_de_telefono = models.CharField(max_length = 50, blank=True, null=True)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
