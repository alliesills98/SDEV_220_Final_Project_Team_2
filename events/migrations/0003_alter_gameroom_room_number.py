# Generated by Django 3.2.18 on 2023-04-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20230420_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameroom',
            name='room_number',
            field=models.CharField(max_length=30, verbose_name='Room Number'),
        ),
    ]
