# Generated by Django 4.1.1 on 2022-09-27 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('secret_identity', models.CharField(max_length=150, unique=True, verbose_name='Identidad secreta')),
                ('age', models.IntegerField(null=True, verbose_name='Edad')),
                ('universe', models.CharField(choices=[('1', 'Marvel'), ('2', 'DC')], max_length=1, verbose_name='Universo')),
            ],
            options={
                'verbose_name': 'Heroe',
                'verbose_name_plural': 'Heroes',
            },
        ),
    ]
