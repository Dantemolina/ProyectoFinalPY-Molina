# Generated by Django 4.2.13 on 2024-06-11 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.DecimalField(decimal_places=0, max_digits=20)),
                ('ciudad_origen_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Cliente.ciudad')),
            ],
        ),
    ]
