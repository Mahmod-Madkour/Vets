# Generated by Django 5.0.1 on 2024-01-30 20:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_category_disease_therapy_replaytherapy'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.category'),
            preserve_default=False,
        ),
    ]
