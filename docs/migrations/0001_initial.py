# Generated by Django 4.2.7 on 2023-12-04 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0014_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('math', 'Mathematics'), ('phys', 'Physics'), ('eng', 'English language'), ('geo', 'Geography'), ('hist', 'History')], max_length=20)),
                ('description', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.studentgroup')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.teacherprofile')),
            ],
        ),
        migrations.CreateModel(
            name='StudentGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=10)),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='docs.lesson')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.studentprofile')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.teacherprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('weekday', models.CharField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday')], default='1', max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('subject', models.CharField(choices=[('math', 'Mathematics'), ('phys', 'Physics'), ('eng', 'English language'), ('geo', 'Geography'), ('hist', 'History')], max_length=20)),
                ('time_slot', models.CharField(choices=[('1', '8:00 - 8:45'), ('2', '9:00 - 9:45'), ('3', '10:00 - 10:45'), ('4', '11:00 - 11:45'), ('5', '12:00 - 12:45'), ('6', '13:00 - 13:45'), ('7', '14:00 - 14:45')], default='1', max_length=20)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.studentgroup')),
                ('lesson', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='docs.lesson')),
            ],
            options={
                'ordering': ['weekday', 'time_slot'],
            },
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('deadline', models.DateField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.lesson')),
            ],
        ),
    ]