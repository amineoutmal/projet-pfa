# Generated by Django 2.0 on 2020-06-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0003_auto_20200623_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervention',
            name='fulladresses',
            field=models.TextField(default=True, max_length=1000),
        ),
    ]