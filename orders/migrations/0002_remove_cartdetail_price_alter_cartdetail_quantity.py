# Generated by Django 4.2.5 on 2023-09-29 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartdetail',
            name='price',
        ),
        migrations.AlterField(
            model_name='cartdetail',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]