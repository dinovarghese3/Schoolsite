# Generated by Django 3.1.1 on 2020-09-22 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicApp', '0010_tbl_answers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_student',
            name='id',
        ),
        migrations.AddField(
            model_name='tbl_answers',
            name='adno',
            field=models.IntegerField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbl_answers',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tbl_student',
            name='admisionno',
            field=models.IntegerField(default='lastname', max_length=20, primary_key=True, serialize=False),
        ),
    ]