# Generated by Django 2.2.5 on 2019-10-13 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0008_auto_20191010_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='car',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='hometown',
        ),
        migrations.RemoveField(
            model_name='user',
            name='preferred_payment',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('preferred_payment', models.CharField(choices=[(1, 'Venmo'), (2, 'Cash'), (3, 'Paypal'), (4, 'Check'), (5, 'Other')], default=1, max_length=6)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rideshare.user')),
            ],
        ),
    ]