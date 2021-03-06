# Generated by Django 3.2.7 on 2022-01-14 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_contactus_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('zip_code', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=500)),
            ],
        ),
    ]
