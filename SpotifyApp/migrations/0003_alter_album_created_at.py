# Generated by Django 4.2.15 on 2024-09-05 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpotifyApp', '0002_alter_album_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
