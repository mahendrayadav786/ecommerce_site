# Generated by Django 3.2.7 on 2022-01-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_updateorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateorder',
            name='timestamp',
            field=models.DateField(),
        ),
    ]
