# Generated by Django 3.1.1 on 2020-10-22 14:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201022_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='price',
            field=models.FloatField(blank=True),
        ),
    ]