# Generated by Django 4.2.1 on 2023-05-26 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('elevator_number', models.IntegerField()),
                ('current_floor', models.IntegerField()),
                ('is_door_open', models.BooleanField(default=True)),
                ('direction', models.CharField(choices=[(1, 'UP'), (-1, 'DOWN'), (0, 'STANDING STILL')], default=0)),
                ('is_operational', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'elevators',
                'db_table': 'elevator',
                'ordering': ['elevator_number'],
            },
        ),
    ]
