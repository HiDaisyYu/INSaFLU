# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IdentifyVirus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(default=0)),
                ('coverage', models.CharField(blank=True, max_length=10, null=True)),
                ('identity', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeqVirus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accession', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ['accession'],
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('path', models.CharField(blank=True, max_length=500, null=True)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='uploaded date')),
                ('abricate_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['version'],
            },
        ),
        migrations.AddField(
            model_name='seqvirus',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seq_virus', to='manage_virus.UploadFile'),
        ),
        migrations.AddField(
            model_name='seqvirus',
            name='kind_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seq_virus', to='manage_virus.Tags'),
        ),
        migrations.AddField(
            model_name='identifyvirus',
            name='seq_virus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='identify_virus', to='manage_virus.SeqVirus'),
        ),
    ]
