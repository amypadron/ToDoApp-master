# Generated by Django 4.2 on 2023-05-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=500)),
                ('fecha_cumplimiento', models.DateField()),
                ('completada', models.BooleanField(default=False)),
            ],
        ),
    ]