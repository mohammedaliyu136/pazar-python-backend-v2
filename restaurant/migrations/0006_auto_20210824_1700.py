# Generated by Django 2.1.3 on 2021-08-24 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='restaurant_fk',
            new_name='restaurant',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user_fk',
            new_name='user',
        ),
    ]