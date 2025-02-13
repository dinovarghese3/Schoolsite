# Generated by Django 3.1.1 on 2020-09-21 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicApp', '0005_tbl_teachers_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=20)),
                ('Lname', models.CharField(max_length=20)),
                ('admisionno', models.IntegerField(max_length=20)),
                ('Age', models.IntegerField(max_length=5)),
                ('dob', models.DateField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('phonenumber', models.IntegerField(max_length=10)),
                ('email', models.CharField(default='......', max_length=30)),
                ('clas', models.IntegerField(max_length=5)),
                ('division', models.CharField(max_length=5)),
                ('dp', models.FileField(blank=True, null=True, upload_to='stud_images', verbose_name='file')),
                ('type', models.CharField(max_length=5)),
                ('password', models.CharField(default=123, max_length=30)),
            ],
        ),
    ]
