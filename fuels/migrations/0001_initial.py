# Generated by Django 5.0 on 2024-11-02 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fuel_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=255)),
                ('petrol_price', models.CharField(max_length=255)),
                ('diesel_price', models.CharField(max_length=255)),
            ],
        ),
    ]
