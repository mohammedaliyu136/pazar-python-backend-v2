# Generated by Django 2.1.3 on 2021-08-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210819_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('contact_number', models.CharField(max_length=30)),
                ('contact_email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=150)),
                ('digital_payment', models.BooleanField()),
                ('cash_payment', models.BooleanField()),
                ('digital_payment_key', models.CharField(max_length=100)),
                ('terms_and_condition', models.CharField(max_length=200)),
                ('privacy_policy', models.CharField(max_length=200)),
                ('about_us', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]