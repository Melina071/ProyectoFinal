# Generated by Django 4.1.3 on 2023-01-02 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppArte', '0009_rename_foto_libros_foto2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libros',
            old_name='foto2',
            new_name='portada',
        ),
    ]
