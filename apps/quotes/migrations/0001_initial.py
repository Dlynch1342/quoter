# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-22 01:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quoteby', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('alias', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='quote',
            name='contributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quoter', to='quotes.User'),
        ),
        migrations.AddField(
            model_name='quote',
            name='favourite',
            field=models.ManyToManyField(related_name='favor', to='quotes.User'),
        ),
    ]