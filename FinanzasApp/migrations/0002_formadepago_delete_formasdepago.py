# Generated by Django 5.0.2 on 2024-03-12 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinanzasApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaDePago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('credito', models.BooleanField()),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='FormasDePago',
        ),
    ]
