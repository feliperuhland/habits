# Generated by Django 4.2.4 on 2023-08-17 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CheckInSymptoms',
            new_name='CheckInSymptom',
        ),
        migrations.RenameModel(
            old_name='Symptoms',
            new_name='Symptom',
        ),
        migrations.RenameField(
            model_name='checkinsymptom',
            old_name='symptoms',
            new_name='symptom',
        ),
    ]
