# Generated by Django 5.0.1 on 2024-01-30 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalgroup',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]