# Generated by Django 4.2.7 on 2023-11-21 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0005_remove_imagen_unique_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Imagen'),
        ),
    ]
