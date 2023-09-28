# Generated by Django 4.2.5 on 2023-09-26 13:51

from django.db import migrations, models
import utils.generate_code


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='code',
            field=models.CharField(default=utils.generate_code.generate_code, max_length=10),
        ),
    ]