# Generated by Django 3.2.8 on 2021-10-25 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_prometheus.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokeball',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Pokeball name')),
                ('level', models.PositiveIntegerField(verbose_name='How match attempt for getting the Pokemon')),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Pokemon name')),
                ('level', models.PositiveIntegerField(verbose_name='Level')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Pokemon Master')),
                ('pokeball', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemons.pokeball', verbose_name='In which pokeball')),
            ],
            bases=(django_prometheus.models.ExportModelOperationsMixin('pokemon'), models.Model),
        ),
    ]
