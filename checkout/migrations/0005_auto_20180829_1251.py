# Generated by Django 2.0.6 on 2018-08-29 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20180829_0731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='country',
        ),
        migrations.RemoveField(
            model_name='order',
            name='county',
        ),
        migrations.RemoveField(
            model_name='order',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street_address_1',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street_address_2',
        ),
        migrations.RemoveField(
            model_name='order',
            name='town_or_city',
        ),
    ]
