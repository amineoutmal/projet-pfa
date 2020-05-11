# Generated by Django 2.0 on 2020-05-11 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technicien',
            name='intervention',
        ),
        migrations.RemoveField(
            model_name='technicien',
            name='societe',
        ),
        migrations.RemoveField(
            model_name='technicien',
            name='typique',
        ),
        migrations.AddField(
            model_name='technicien',
            name='type',
            field=models.CharField(choices=[('Interne', 'Interne'), ('Externe', 'Externe')], max_length=200, null=True),
        ),
    ]
