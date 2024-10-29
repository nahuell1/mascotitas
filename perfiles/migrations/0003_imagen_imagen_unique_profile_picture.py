# Generated by Django 4.0.4 on 2022-05-07 15:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0002_alter_perfil_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='images/')),
                ('descripcion', models.TextField(blank=True, max_length=500)),
                ('is_profile_picture', models.BooleanField(default=False)),
                ('perfil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='perfiles.perfil')),
            ],
        ),
        migrations.AddConstraint(
            model_name='imagen',
            constraint=models.UniqueConstraint(fields=('id', 'is_profile_picture'), name='unique_profile_picture'),
        ),
    ]
