# Generated by Django 2.1.3 on 2021-08-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_auto_20210825_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='pending', max_length=11),
        ),
    ]
