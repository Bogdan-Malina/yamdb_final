# Generated by Django 2.2.16 on 2022-07-25 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220726_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(max_length=256, null=True, unique=True),
        ),
    ]
