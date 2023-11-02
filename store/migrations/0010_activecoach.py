# Generated by Django 4.2.6 on 2023-11-01 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_activeticket_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveCoach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('amount_of_training', models.IntegerField()),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.coach')),
            ],
        ),
    ]
