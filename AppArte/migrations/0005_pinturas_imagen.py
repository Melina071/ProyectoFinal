# Generated by Django 4.1.3 on 2023-01-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppArte', '0004_discos_usuarioblog_pinturas_usuarioblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='pinturas',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='pinturas'),
        ),
    ]
