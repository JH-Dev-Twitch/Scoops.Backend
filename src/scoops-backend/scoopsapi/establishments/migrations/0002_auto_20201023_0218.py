# Generated by Django 3.0.5 on 2020-10-23 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='establishmenttype',
            table='establishments_types',
        ),
    ]
