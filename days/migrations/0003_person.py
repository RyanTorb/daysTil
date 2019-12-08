# Generated by Django 2.2.6 on 2019-12-07 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('days', '0002_auto_20191122_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Adam', 'Adam'), ('Jack', 'Jack'), ('Reid', 'Reid'), ('Ryan', 'Ryan'), ('Trevor', 'Trevor'), ('Will', 'Will'), ('William', 'William')], default=1, max_length=8)),
                ('queue', models.IntegerField(default=None, null=True)),
                ('notes', models.CharField(default=None, max_length=200, null=True)),
            ],
        ),
    ]
