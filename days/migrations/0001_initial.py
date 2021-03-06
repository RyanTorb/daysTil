# Generated by Django 2.2.6 on 2019-11-22 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(default=None, max_length=10, null=True)),
                ('car', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
                ('preferred_payment', models.CharField(choices=[('Venmo', 'Venmo'), ('Cashapp', 'Cashapp'), ('Cash', 'Cash'), ('Paypal', 'Paypal'), ('Check', 'Check'), ('Other', 'Other')], default=1, max_length=7)),
                ('User', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
