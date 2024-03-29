# Generated by Django 4.0.6 on 2022-07-20 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.PositiveBigIntegerField(default=0, unique=True, verbose_name='Numero de cuenta')),
                ('alias', models.CharField(max_length=30, unique=True)),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Saldo')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Cuenta',
                'verbose_name_plural': 'Cuentas',
            },
        ),
    ]
