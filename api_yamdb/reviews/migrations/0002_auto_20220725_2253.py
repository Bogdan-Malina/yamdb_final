# Generated by Django 2.2.16 on 2022-07-25 19:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(10, 'Оценка не может превышать 10'), django.core.validators.MinValueValidator(1)], verbose_name='Оценка'),
        ),
    ]
