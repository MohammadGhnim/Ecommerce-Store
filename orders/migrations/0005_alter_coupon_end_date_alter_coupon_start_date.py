# Generated by Django 4.2.5 on 2023-10-08 13:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_cartdetail_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
