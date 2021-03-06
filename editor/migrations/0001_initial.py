# Generated by Django 3.1.6 on 2021-02-11 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('legal_name', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=15)),
                ('address_loc', models.CharField(max_length=100)),
                ('address_number', models.IntegerField()),
                ('address_cep', models.CharField(max_length=9)),
                ('address_city', models.CharField(max_length=100)),
                ('address_state', models.CharField(max_length=2)),
            ],
        ),
    ]
