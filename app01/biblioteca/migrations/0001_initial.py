# Generated by Django 4.2.1 on 2023-05-07 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Editorial')),
                ('adress', models.CharField(max_length=255, verbose_name='Direccion')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefono')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('country', models.CharField(max_length=100, verbose_name='Pais')),
            ],
        ),
    ]
