# Generated by Django 4.0.6 on 2022-07-20 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='transaction',
            field=models.ManyToManyField(null=True, related_name='History', to='transaction.transaction'),
        ),
    ]