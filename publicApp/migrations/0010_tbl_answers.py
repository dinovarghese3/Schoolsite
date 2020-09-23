# Generated by Django 3.1.1 on 2020-09-22 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicApp', '0009_tbl_questin'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('clas', models.IntegerField(max_length=5)),
                ('division', models.CharField(max_length=5)),
                ('qid', models.CharField(max_length=50)),
                ('sdate', models.CharField(max_length=20)),
                ('answes', models.FileField(blank=True, null=True, upload_to='answers', verbose_name='file')),
            ],
        ),
    ]