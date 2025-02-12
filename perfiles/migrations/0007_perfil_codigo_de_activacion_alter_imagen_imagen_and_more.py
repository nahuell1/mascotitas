# Generated by Django 4.2.7 on 2023-11-21 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0006_alter_imagen_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='codigo_de_activacion',
            field=models.CharField(default='jnf7Ckg70V', max_length=10),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='imagen'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='nombre',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
