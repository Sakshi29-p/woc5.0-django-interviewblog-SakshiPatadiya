# Generated by Django 4.1.5 on 2023-01-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='grad_year',
            field=models.FloatField(null=True),
        ),
    ]
