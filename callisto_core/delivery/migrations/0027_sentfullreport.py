# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 14:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("delivery", "0026_auto_20171122_1446")]

    operations = [
        migrations.CreateModel(
            name="SentFullReport",
            fields=[],
            options={"proxy": True, "indexes": []},
            bases=("delivery.newsentfullreport",),
        )
    ]
