# Generated by Django 3.2.15 on 2022-10-25 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadEconomica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacidadPago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('capacidadAhorro', models.DecimalField(decimal_places=2, max_digits=10)),
                ('asociaciones', models.CharField(max_length=50)),
                ('lugarTrabajo', models.CharField(max_length=50)),
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
                ('avatar', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('codigo', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=3)),
                ('telefono', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Parentesco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEjecutivo', models.CharField(max_length=60)),
                ('fecha', models.DateField()),
                ('lugar', models.CharField(max_length=60)),
                ('id_ejecutivo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.ejecutivo')),
            ],
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('area', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UsoInmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
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
                ('fechaNacim', models.DateField()),
                ('numeroDocumento', models.CharField(max_length=10)),
                ('nit', models.CharField(max_length=12)),
                ('isss', models.CharField(max_length=12)),
                ('tipoTrabajador', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=10)),
                ('situacionSolicitante', models.CharField(max_length=10)),
                ('foto', models.ImageField(upload_to='')),
                ('firma', models.ImageField(upload_to='')),
                ('id_actividadEconomica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_gestor_asociados.actividadeconomica')),
                ('id_conyuge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_gestor_asociados.conyuge')),
                ('id_domicilio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_gestor_asociados.domicilio')),
                ('id_estadoCivil', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.estadocivil')),
                ('id_genero', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.genero')),
                ('id_nacionalidad', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.pais')),
                ('id_registro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_gestor_asociados.registro')),
                ('id_tipoDocumento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.tipodocumento')),
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
                ('id_solicitante', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.tipodocumento')),
            ],
        ),
        migrations.AddField(
            model_name='domicilio',
            name='usoInmueble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.usoinmueble'),
        ),
        migrations.AddField(
            model_name='conyuge',
            name='id_tipoDocumento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.tipodocumento'),
        ),
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('edad', models.IntegerField()),
                ('porcentajeBenef', models.DecimalField(decimal_places=2, max_digits=4)),
                ('id_parentesco', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.parentesco')),
                ('id_solicitante', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.solicitante')),
            ],
        ),
        migrations.AddField(
            model_name='actividadeconomica',
            name='rubro_profesion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sistema_gestor_asociados.rubro'),
        ),
    ]
