# Generated by Django 4.1.5 on 2023-01-19 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogtagindexpage_blogcategory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogCategory',
        ),
    ]