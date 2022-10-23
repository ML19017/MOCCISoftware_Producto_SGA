# Generated by Django 3.2.15 on 2022-10-23 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadEconomica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rubro_profesion', models.CharField(max_length=50)),
                ('capacidadPago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('capacidadAhorro', models.DecimalField(decimal_places=2, max_digits=10)),
                ('asociaciones', models.CharField(max_length=50)),
                ('lugarTrabajo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('edad', models.IntegerField()),
                ('parentesco', models.CharField(max_length=15)),
                ('porcentajeBenef', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Conyuge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=35)),
                ('apellidos', models.CharField(max_length=15)),
                ('fechaNacim', models.DateField()),
                ('empresa', models.CharField(max_length=30)),
                ('cargo', models.CharField(max_length=20)),
                ('numeroDocumento', models.CharField(max_length=10)),
                ('telefonoCelular', models.CharField(max_length=10)),
                ('telefonoOficina', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=150)),
                ('numeroCasaDepart', models.IntegerField()),
                ('usoInmueble', models.CharField(max_length=150)),
                ('tiempo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ejecutivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=70)),
                ('telefono', models.IntegerField()),
                ('correoElec', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEjecutivo', models.CharField(max_length=60)),
                ('fecha', models.DateField()),
                ('lugar', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoAsociado', models.CharField(max_length=10)),
                ('nombres', models.CharField(max_length=35)),
                ('primerApellido', models.CharField(max_length=15)),
                ('segundoApellido', models.CharField(max_length=15)),
                ('apellidoCasada', models.CharField(max_length=15)),
                ('genero', models.CharField(max_length=10)),
                ('fechaNacim', models.DateField()),
                ('estadoCivil', models.CharField(max_length=10)),
                ('nit', models.CharField(max_length=12)),
                ('numeroDocumento', models.CharField(max_length=10)),
                ('isss', models.CharField(max_length=12)),
                ('tipoDocumento', models.CharField(max_length=10)),
                ('tipoTrabajador', models.CharField(max_length=10)),
                ('dreccion', models.CharField(max_length=10)),
                ('situacionSolicitante', models.CharField(max_length=10)),
            ],
        ),
    ]
