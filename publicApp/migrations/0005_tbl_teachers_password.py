# Generated by Django 3.1.1 on 2020-09-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicApp', '0004_auto_20200920_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_teachers',
            name='password',
            field=models.CharField(default=123, max_length=30),
        ),
    ]
