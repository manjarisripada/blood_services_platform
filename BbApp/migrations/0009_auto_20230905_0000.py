# Generated by Django 3.0 on 2023-09-04 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BbApp', '0008_donate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donate',
            old_name='dtatus',
            new_name='status',
        ),
    ]
