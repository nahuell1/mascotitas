import uuid
from django.db import models
from django.utils.crypto import get_random_string
from users.models import User


def generate_random_string():
    return get_random_string(12)


class Perfil(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length = 200, blank=False, null=True)
    numero_de_telefono = models.CharField(
        max_length = 50,
        blank=True,
        null=True,
        help_text="Este número podría servir para contactar a su humano en caso de que se extravíe."
    )
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    ubicacion = models.CharField(max_length=255, blank=True)
    biografia = models.TextField(max_length=500, blank=True)
    fecha_de_creacion = models.DateField(auto_now_add=True, db_index=True, blank=True, null=True)
    humano = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    codigo_de_activacion = models.CharField(max_length=10, default=generate_random_string)

    @property
    def profile_picture(self):
        return self.imagenes.filter(is_profile_picture=True).first()

    def __str__(self):
        if self.nombre:
            return self.nombre
        return id


class Imagen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    perfil = models.ForeignKey(Perfil, on_delete = models.CASCADE, related_name='imagenes', null=True, blank=True)
    imagen = models.ImageField(verbose_name='imagen', upload_to='images/', null=True, blank=True)
    descripcion = models.TextField(max_length=500, blank=True)
    is_profile_picture = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['perfil', 'is_profile_picture'], name="unique_profile_picture")
        ]
