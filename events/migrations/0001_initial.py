# Generated by Django 5.1 on 2024-09-02 01:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('event_type', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField()),
                ('details', models.JSONField(blank=True, default=dict, null=True)),
            ],
        ),
    ]
