# Generated by Django 3.2.18 on 2023-04-22 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_gameroom_is_full'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameroom',
            name='owner',
            field=models.IntegerField(default=1),
        ),
    ]
