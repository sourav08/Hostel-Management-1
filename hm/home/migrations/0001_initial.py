# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 23:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('type', models.CharField(default=b'', max_length=100)),
                ('complaint', models.CharField(default=b'', max_length=100)),
                ('time', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=100, unique=True)),
                ('fullname', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('designation', models.CharField(default=b'', max_length=100)),
                ('address', models.CharField(default=b'', max_length=100)),
                ('email', models.EmailField(default=b'example@example.com', max_length=254)),
                ('hostel', models.ForeignKey(default=b'', on_delete=django.db.models.deletion.PROTECT, to='home.Hostel')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll', models.BigIntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('dob', models.DateField(default=b'1/1/1996')),
                ('email', models.EmailField(default=b'example@example.com', max_length=254)),
                ('mobile', models.BigIntegerField(default=0)),
                ('program', models.CharField(choices=[(b'BTECH', b'B.Tech'), (b'IDD', b'IDD'), (b'IMD', b'IMD'), (b'MTECH', b'M.Tech'), (b'PHD', b'Phd')], default=b'', max_length=10)),
                ('department', models.CharField(choices=[(b'CSE', b'Computer Science & Engg'), (b'MECH', b'Mechanical Engg'), (b'CIV', b'Civil Engg'), (b'MNC', b'Mathematics & Computing'), (b'EEE', b'Electrical Engg')], default=b'', max_length=10)),
                ('semester', models.IntegerField(choices=[(1, b'I'), (2, b'II'), (3, b'III'), (4, b'IV'), (5, b'V'), (6, b'VI'), (7, b'VII'), (8, b'VIII'), (9, b'IX'), (10, b'X')], default=0)),
                ('father_name', models.CharField(default=b'', max_length=100)),
                ('mother_name', models.CharField(default=b'', max_length=100)),
                ('father_occ', models.CharField(default=b'', max_length=100)),
                ('mother_occ', models.CharField(default=b'', max_length=100)),
                ('parent_contact', models.BigIntegerField(default=0)),
                ('room', models.CharField(default=b'', max_length=10)),
                ('du', models.CharField(default=b'', max_length=100)),
                ('mess_du', models.CharField(default=b'', max_length=100)),
                ('guardian_name', models.CharField(blank=True, max_length=100, null=True)),
                ('local_address', models.CharField(blank=True, max_length=500, null=True)),
                ('relation', models.CharField(blank=True, max_length=100, null=True)),
                ('guardian_contact', models.BigIntegerField(blank=True, default=0, null=True)),
                ('permanent_address', models.CharField(default=b'', max_length=500)),
                ('town', models.CharField(default=b'', max_length=100)),
                ('state', models.CharField(default=b'', max_length=100)),
                ('pincode', models.IntegerField(default=0)),
                ('account', models.BigIntegerField(default=0)),
                ('bank_name', models.CharField(default=b'', max_length=100)),
                ('branch_name', models.CharField(default=b'', max_length=100)),
                ('ifsc', models.CharField(default=b'', max_length=100)),
                ('password', models.CharField(default=b'', max_length=100)),
                ('hostel', models.ForeignKey(default=b'', on_delete=django.db.models.deletion.PROTECT, to='home.Hostel')),
            ],
        ),
        migrations.AddField(
            model_name='complaint',
            name='hostel',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='home.Hostel'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='student',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='home.Student'),
        ),
    ]