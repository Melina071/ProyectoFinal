# Generated by Django 4.1.3 on 2023-01-02 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppArte', '0010_rename_foto2_libros_portada'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discos',
            old_name='imagen',
            new_name='tapa',
        ),
    ]
