# Generated by Django 5.0.1 on 2024-02-03 17:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_search_random_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='uuid_field',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
