# Generated by Django 4.2.3 on 2023-07-25 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_remove_student_registered_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='registered',
            field=models.BooleanField(default=False),
        ),
    ]
