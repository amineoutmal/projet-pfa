# Generated by Django 2.0 on 2020-06-05 15:15

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=8)),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=32)),
                ('privelege', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Affectation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_affectation', models.DateField(auto_now_add=True)),
                ('date_resolution', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=8)),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=32)),
                ('matricule_id', models.CharField(max_length=200)),
                ('adresse', models.CharField(max_length=600)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.FloatField()),
                ('QTE', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_equipement', models.CharField(max_length=60)),
                ('qte_stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fourniseur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=8)),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=32)),
                ('materiel_demander', models.CharField(max_length=60)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titre_intervention', models.TextField(max_length=255)),
                ('date_intervention', models.DateField(auto_now_add=True)),
                ('etat', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='medial/%Y/%m/%D')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('clients', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='globals.Client')),
                ('equipements', models.ManyToManyField(to='globals.Equipement')),
            ],
        ),
        migrations.CreateModel(
            name='Panne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_panne', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Technicien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=8)),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=32)),
                ('types', models.CharField(choices=[('Interne', 'Interne'), ('Externe', 'Externe')], default=True, max_length=100)),
                ('disponibilité', models.CharField(default=True, max_length=100)),
                ('specialité', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='globals.Panne')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='intervention',
            name='type_panne',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.Panne'),
        ),
        migrations.AddField(
            model_name='equipement',
            name='panne',
            field=models.ManyToManyField(to='globals.Panne'),
        ),
        migrations.AddField(
            model_name='commande',
            name='equipement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.Equipement'),
        ),
        migrations.AddField(
            model_name='commande',
            name='fourniseur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.Fourniseur'),
        ),
        migrations.AddField(
            model_name='affectation',
            name='Inter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.Intervention'),
        ),
        migrations.AddField(
            model_name='affectation',
            name='tech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.Technicien'),
        ),
    ]
