# Generated by Django 3.0.7 on 2020-07-01 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filters_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Filters',
            new_name='Filter',
        ),
    ]
