# Generated by Django 2.2.6 on 2019-10-11 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0007_auto_20191010_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=200),
        ),
    ]
