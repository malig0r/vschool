# Generated by Django 4.2.7 on 2023-12-03 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_studentprofile_group_alter_studentprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('std', 'Student'), ('tchr', 'Teacher'), ('grd', 'Guardian')], default='tchr', max_length=10),
        ),
    ]