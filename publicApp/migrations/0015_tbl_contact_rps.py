# Generated by Django 3.0.5 on 2020-09-28 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicApp', '0014_tbl_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_contact',
            name='rps',
            field=models.CharField(default='replay', max_length=10),
        ),
    ]