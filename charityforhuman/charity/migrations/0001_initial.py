# Generated by Django 4.1.5 on 2023-01-19 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='charity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doner_name', models.CharField(max_length=50)),
                ('doner_address', models.CharField(max_length=100)),
                ('doner_email', models.EmailField(max_length=30)),
                ('doner_mob', models.IntegerField(max_length=15)),
            ],
        ),
    ]
