# Generated by Django 4.2.3 on 2023-07-27 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appClinica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='masCodigo',
            field=models.CharField(db_comment='Código único asignado a la mascota', max_length=15, unique=True),
        ),
    ]