# Generated by Django 2.0 on 2020-05-11 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technicien',
            name='societe',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
