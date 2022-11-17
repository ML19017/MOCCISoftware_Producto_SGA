# Generated by Django 3.2.15 on 2022-11-17 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asociado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_identidad', models.CharField(default='no especificado', max_length=120)),
                ('isss', models.CharField(max_length=120, null=True)),
                ('nit', models.CharField(max_length=120, null=True)),
                ('nup', models.CharField(max_length=120, null=True)),
                ('fecha_nacimiento', models.DateField(default='2000-1-1')),
                ('nombres', models.CharField(default='no especificado', max_length=120)),
                ('primer_apellido', models.CharField(default='no especificado', max_length=50)),
                ('segundo_apellido', models.CharField(default='no especificado', max_length=50)),
                ('apellido_casada', models.CharField(max_length=50, null=True)),
                ('salario', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('estado_aprobado', models.BooleanField(default=False)),
                ('estado_pagado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoFamiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('alfa_2', models.CharField(max_length=2)),
                ('alfa_3', models.CharField(max_length=3)),
                ('alfa_numerico', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Parentesco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoTrabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UsoInmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ejecutivo', models.CharField(max_length=120)),
                ('fecha', models.DateField()),
                ('asociado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.asociado')),
            ],
        ),
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='no especificado', max_length=120)),
                ('telefono_personal', models.CharField(default='no especificado', max_length=120)),
                ('correo_personal', models.EmailField(default='no especificado', max_length=120)),
                ('tipo', models.BooleanField()),
                ('asociado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_gestor_asociados.asociado')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(default='no especificado', max_length=120)),
                ('domicilio', models.CharField(default='no especificado', max_length=120)),
                ('ubicacion_geografica', models.CharField(default='no especificado', max_length=120)),
                ('tiempo', models.SmallIntegerField(default=0)),
                ('asociado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_gestor_asociados.asociado')),
                ('uso_inmueble', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.usoinmueble')),
            ],
        ),
        migrations.CreateModel(
            name='Conyuge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(default='no especificado', max_length=120)),
                ('apellidos', models.CharField(default='no especificado', max_length=120)),
                ('fecha_nacimiento', models.DateField(default='2000-1-1')),
                ('empresa', models.CharField(default='no especificado', max_length=50)),
                ('cargo', models.CharField(default='no especificado', max_length=50)),
                ('numero_documento', models.CharField(default='no especificado', max_length=120)),
                ('telefono_personal', models.CharField(default='no especificado', max_length=50)),
                ('telefono_oficina', models.CharField(default='no especificado', max_length=50)),
                ('correo', models.EmailField(default='no especificado', max_length=120)),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.tipodocumento')),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=120)),
                ('apellidos', models.CharField(max_length=120)),
                ('edad', models.SmallIntegerField(default=0)),
                ('porcentaje', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('asociado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_gestor_asociados.asociado')),
                ('parentesco', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.parentesco')),
            ],
        ),
        migrations.AddField(
            model_name='asociado',
            name='conyuge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema_gestor_asociados.conyuge'),
        ),
        migrations.AddField(
            model_name='asociado',
            name='estado_familiar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.estadofamiliar'),
        ),
        migrations.AddField(
            model_name='asociado',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.genero'),
        ),
        migrations.AddField(
            model_name='asociado',
            name='nacionalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='nacionalidad', to='sistema_gestor_asociados.pais'),
        ),
        migrations.AddField(
            model_name='asociado',
            name='pais_nacimiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='pais_nacimiento', to='sistema_gestor_asociados.pais'),
        ),
        migrations.AddField(
            model_name='asociado',
            name='tipo_documento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.tipodocumento'),
        ),
        migrations.AddField(
            model_name='asociado',
            name='tipo_trabajador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.tipotrabajador'),
        ),
    ]
