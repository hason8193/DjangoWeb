# Generated by Django 5.0.3 on 2024-03-21 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_remove_medicalreport_patient_medicalreport_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalreport',
            name='way',
            field=models.CharField(choices=[('1', 'Way 1'), ('2', 'Way 2'), ('3', 'Way 3'), ('4', 'Way 4')], max_length=100),
        ),
    ]