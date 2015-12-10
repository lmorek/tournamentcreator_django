# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-10 18:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamName', models.CharField(max_length=200)),
                ('capitan', models.CharField(max_length=200)),
                ('firstPlayer', models.CharField(max_length=200)),
                ('secondPlayer', models.CharField(max_length=200)),
                ('thirdPlayer', models.CharField(max_length=200)),
                ('fourthplayer', models.CharField(max_length=200)),
                ('fifthPlayer', models.CharField(max_length=200)),
                ('sixthplayer', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
