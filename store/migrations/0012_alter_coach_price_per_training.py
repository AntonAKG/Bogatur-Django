# Generated by Django 4.2.6 on 2023-11-02 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_activecoach_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='price_per_training',
            field=models.IntegerField(max_length=10),
        ),
    ]