# Generated by Django 5.0.3 on 2024-03-10 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_delete_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientrecord',
            name='gender',
            field=models.CharField(default='', max_length=100),
        ),
    ]