# Generated by Django 4.1.5 on 2023-01-25 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_profesor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='apellido',
            new_name='apellidos',
        ),
    ]