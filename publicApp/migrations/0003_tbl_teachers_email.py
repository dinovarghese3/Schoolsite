# Generated by Django 3.1.1 on 2020-09-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicApp', '0002_tbl_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_teachers',
            name='email',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
