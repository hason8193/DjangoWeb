# Generated by Django 5.0.3 on 2024-05-12 09:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_detailedpatientlist_medicalexamination_medication_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalexamination',
            name='medicine',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.medication'),
        ),
    ]