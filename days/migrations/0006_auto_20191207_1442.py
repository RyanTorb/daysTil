# Generated by Django 2.2.6 on 2019-12-07 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('days', '0005_auto_20191207_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='User',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]