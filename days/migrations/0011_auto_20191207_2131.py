# Generated by Django 2.2.6 on 2019-12-08 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('days', '0010_room_original'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='original',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='selected',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
