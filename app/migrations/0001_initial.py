# Generated by Django 3.2.8 on 2021-10-05 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive_no', models.CharField(blank=True, max_length=200, null=True)),
                ('invalid_no', models.CharField(blank=True, max_length=200, null=True)),
                ('min_no', models.CharField(blank=True, max_length=200, null=True)),
                ('max_no', models.IntegerField(blank=True, max_length=200, null=True)),
                ('avg', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
