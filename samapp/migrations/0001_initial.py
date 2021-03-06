# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 15:58
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='areas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='city_areamap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samapp.areas')),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samapp.cities')),
            ],
        ),
        migrations.CreateModel(
            name='dress_servicemap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='dresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dresses', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='excess_cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(max_length=50)),
                ('cost', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='laundries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laundry_name', models.CharField(max_length=20)),
                ('phno', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('city_areamapid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samapp.city_areamap')),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('phno', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('dress_servicemapid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samapp.dress_servicemap')),
                ('excess_costid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samapp.excess_cost')),
                ('laundry_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samapp.laundries')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('mobile', models.CharField(blank=True, default=None, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectors', models.CharField(max_length=50)),
                ('images', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='laundries',
            name='sector_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samapp.sectors'),
        ),
        migrations.AddField(
            model_name='excess_cost',
            name='laundry_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samapp.laundries'),
        ),
        migrations.AddField(
            model_name='dress_servicemap',
            name='dress_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samapp.dresses'),
        ),
        migrations.AddField(
            model_name='dress_servicemap',
            name='laundry_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samapp.laundries'),
        ),
        migrations.AddField(
            model_name='dress_servicemap',
            name='service_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samapp.services'),
        ),
    ]
