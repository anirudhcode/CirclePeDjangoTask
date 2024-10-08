# Generated by Django 5.1 on 2024-09-02 01:17

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpaceStations',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spacestations', to='planets.planets')),
            ],
        ),
    ]
