# Generated by Django 5.0.3 on 2024-05-21 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_medicationstocklist_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=10),
            preserve_default=False,
        ),
    ]
