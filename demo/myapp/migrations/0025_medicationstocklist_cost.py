# Generated by Django 5.0.3 on 2024-05-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_remove_medicationstocklist_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicationstocklist',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
