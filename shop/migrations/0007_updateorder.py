# Generated by Django 3.2.7 on 2022-01-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateOrder',
            fields=[
                ('update_id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default=0)),
                ('update_desc', models.CharField(max_length=100)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
