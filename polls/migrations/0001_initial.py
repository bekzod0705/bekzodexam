# Generated by Django 4.2.5 on 2023-09-12 09:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='authorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60)),
                ('lastname', models.CharField(default='', max_length=60)),
                ('birthday', models.DateTimeField()),
                ('ismarried', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='bookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60)),
                ('page', models.IntegerField(default=0)),
                ('desc', models.TextField(default='write!')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.authormodel')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]