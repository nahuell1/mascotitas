# Generated by Django 3.2.7 on 2022-04-30 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('numero_de_telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_de_nacimiento', models.DateField(blank=True, null=True)),
                ('ubicacion', models.CharField(blank=True, max_length=255)),
                ('biografia', models.TextField(blank=True, max_length=500)),
                ('fecha_de_creacion', models.DateField(auto_now_add=True, db_index=True, null=True)),
                ('humano', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
