# Generated by Django 2.0 on 2020-06-06 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0002_auto_20200605_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervention',
            name='fulladresses',
            field=models.TextField(default=True, max_length=500),
        ),
    ]
