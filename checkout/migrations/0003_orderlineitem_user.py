# Generated by Django 2.0.6 on 2018-08-28 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0002_orderlineitem_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
