# Generated by Django 4.2.7 on 2023-12-04 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0003_rename_date_time_lesson_time_slot'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homework',
            options={'ordering': ['deadline']},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['time_slot']},
        ),
    ]