# Generated by Django 2.2.1 on 2022-03-13 04:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_consumer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Consumer',
            new_name='Consume',
        ),
    ]
