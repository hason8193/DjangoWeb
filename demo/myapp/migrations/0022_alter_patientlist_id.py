# Generated by Django 5.0.3 on 2024-05-14 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_alter_patientlist_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientlist',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
