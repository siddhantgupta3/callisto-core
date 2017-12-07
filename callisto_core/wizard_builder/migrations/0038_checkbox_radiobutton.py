# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 06:08
from __future__ import unicode_literals

from django.db import migrations

import wizard_builder.model_helpers


class Migration(migrations.Migration):

    dependencies = [
        ('wizard_builder', '0037_auto_20171028_0142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkbox',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=(
                wizard_builder.model_helpers.ProxyQuestion,
                'wizard_builder.formquestion'),
        ),
        migrations.CreateModel(
            name='RadioButton',
            fields=[],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=(
                wizard_builder.model_helpers.ProxyQuestion,
                'wizard_builder.formquestion'),
        ),
    ]
