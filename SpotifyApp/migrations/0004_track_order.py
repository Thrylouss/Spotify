# Generated by Django 4.2.15 on 2024-09-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpotifyApp', '0003_alter_album_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]