# Generated by Django 4.2.7 on 2023-12-15 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('docs', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentgrade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.studentprofile'),
        ),
        migrations.AddField(
            model_name='studentgrade',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.teacherprofile'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.studentgroup'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson', to='users.studentgroup'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='schedule',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='docs.schedule'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.teacherprofile'),
        ),
        migrations.AddField(
            model_name='homework',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.lesson'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='lesson',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to='docs.lesson'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='students',
            field=models.ManyToManyField(to='users.studentprofile'),
        ),
    ]
