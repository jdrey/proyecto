# Generated by Django 4.1.3 on 2022-11-06 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_equipos_equipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='ciudad',
            field=models.CharField(max_length=200, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='titulos',
            field=models.CharField(max_length=200, verbose_name='Títulos'),
        ),
    ]