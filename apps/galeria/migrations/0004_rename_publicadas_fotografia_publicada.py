# Generated by Django 4.2.7 on 2023-12-01 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicadas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='publicadas',
            new_name='publicada',
        ),
    ]
