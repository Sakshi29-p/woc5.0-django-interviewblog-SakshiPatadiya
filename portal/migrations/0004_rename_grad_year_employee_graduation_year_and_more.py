# Generated by Django 4.1.5 on 2023-01-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_employee_password_employee_prog_study_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='grad_year',
            new_name='graduation_year',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='prog_study',
            new_name='program_of_study',
        ),
        migrations.AddField(
            model_name='employee',
            name='degree',
            field=models.CharField(choices=[('ICT', 'ICT'), ('ICT+CS', 'ICT+CS'), ('MNC', 'MNC')], max_length=200, null=True),
        ),
    ]
