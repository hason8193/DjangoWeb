# Generated by Django 5.0.3 on 2024-05-21 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_medicalexamination_med'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalexamination',
            name='patientlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.patientlist'),
        ),
    ]