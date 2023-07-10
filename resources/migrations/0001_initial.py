# Generated by Django 4.2.3 on 2023-07-10 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Batch_name', models.CharField(max_length=220)),
            ],
            options={
                'verbose_name_plural': 'Batches',
            },
        ),
        migrations.CreateModel(
            name='Comp_Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Computer Brands',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.CharField(max_length=220)),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TrainerName', models.CharField(max_length=220)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.course')),
            ],
            options={
                'verbose_name_plural': 'Trainers',
            },
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comp_code', models.CharField(max_length=50)),
                ('Category', models.IntegerField(choices=[(0, 'Laptop'), (1, 'Desktop')])),
                ('Type', models.IntegerField(choices=[(0, 'owned'), (1, 'rented')])),
                ('Assigned_trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.trainer')),
                ('Brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.comp_brand')),
            ],
        ),
    ]
