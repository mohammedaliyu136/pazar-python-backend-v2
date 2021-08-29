# Generated by Django 2.1.3 on 2021-08-29 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0018_order_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('discount_type', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=30)),
                ('discount', models.FloatField()),
                ('min_purchase', models.FloatField()),
                ('max_discount', models.FloatField()),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('expire_date', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
