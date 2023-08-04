# Generated by Django 4.2.3 on 2023-07-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appClinica', '0003_alter_mascota_masfecnacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementosubtiporemision',
            name='eleSubTipRemNombre',
            field=models.CharField(db_comment='Nombre del subtipo de elemento de la remision ej:Hemograma', max_length=100),
        ),
        migrations.AlterField(
            model_name='tiporemision',
            name='tipoRemNombre',
            field=models.CharField(db_comment='Nombre del tipo de remision ej:Examen Laboratorio', max_length=100),
        ),
    ]