# Generated by Django 4.2.3 on 2023-07-30 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appClinica', '0005_alter_servicios_sertipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userTipo',
            field=models.CharField(choices=[('Administrador', 'Administrador'), ('Veterinario', 'Veterinario'), ('Auxiliar', 'Auxiliar'), ('Cliente', 'Cliente')], db_comment='Nombre Tipo de usuario', max_length=18),
        ),
    ]
