# Generated by Django 2.1.7 on 2019-06-04 20:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rainforest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
