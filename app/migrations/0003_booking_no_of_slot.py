# Generated by Django 3.2.8 on 2021-10-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='no_of_slot',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]