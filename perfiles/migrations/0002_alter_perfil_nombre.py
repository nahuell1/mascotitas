# Generated by Django 3.2.7 on 2022-05-01 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='nombre',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
