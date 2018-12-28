# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-16 06:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sl_sm', '0003_auto_20181216_0616'),
    ]

    operations = [
        migrations.CreateModel(
            name='discounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankname', models.CharField(max_length=15)),
                ('discountPercent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='discounts',
            name='p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sl_sm.product'),
        ),
    ]