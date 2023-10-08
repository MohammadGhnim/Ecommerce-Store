# Generated by Django 4.2.5 on 2023-10-08 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_coupon_end_date_alter_coupon_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_coupon', to='orders.coupon'),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_with_coupon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_coupon', to='orders.coupon'),
        ),
        migrations.AddField(
            model_name='order',
            name='total_with_coupon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
