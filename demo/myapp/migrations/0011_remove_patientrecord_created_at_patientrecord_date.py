# Generated by Django 5.0.3 on 2024-03-11 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_patientrecord_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientrecord',
            name='created_at',
        ),
        migrations.AddField(
            model_name='patientrecord',
            name='date',
            field=models.DateField(default='1970-01-01'),
        ),
    ]
