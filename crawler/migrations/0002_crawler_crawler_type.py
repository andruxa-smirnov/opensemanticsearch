# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-04-04 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawler',
            name='crawler_type',
            field=models.CharField(choices=[('PAGE', 'Index only this web page'), ('PATH', 'Crawl all web pages within this path'), ('DOMAIN', 'Crawl full domain and subdomains')], default='PATH', max_length=6),
        ),
    ]
