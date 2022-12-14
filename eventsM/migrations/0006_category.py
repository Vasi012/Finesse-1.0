# Generated by Django 3.2.15 on 2022-10-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):
    """Migrations to the DB"""
    dependencies = [
        ('eventsM', '0005_auto_20221009_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]
