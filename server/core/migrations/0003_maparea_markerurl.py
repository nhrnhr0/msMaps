# Generated by Django 4.0.3 on 2022-04-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_mappoint_area_alter_mappoint_lat'),
    ]

    operations = [
        migrations.AddField(
            model_name='maparea',
            name='markerUrl',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
