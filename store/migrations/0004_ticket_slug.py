# Generated by Django 4.2.6 on 2023-10-22 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_basketticket_basketcoach'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
