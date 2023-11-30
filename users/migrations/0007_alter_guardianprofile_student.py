# Generated by Django 4.2.7 on 2023-11-26 20:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_teacherprofile_invite_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardianprofile',
            name='student',
            field=models.ManyToManyField(blank=True, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
    ]
