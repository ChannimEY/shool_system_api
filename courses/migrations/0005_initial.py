# Generated by Django 5.2.3 on 2025-06-24 04:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0004_delete_course_delete_teacher'),
        ('teachers', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('teacher_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='teachers.teacher')),
            ],
        ),
    ]
