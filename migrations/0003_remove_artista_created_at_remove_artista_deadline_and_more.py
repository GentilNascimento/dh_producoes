# Generated by Django 5.0.4 on 2024-04-25 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artista', '0002_artista_created_at_artista_deadline_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artista',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='finished_at',
        ),
    ]
