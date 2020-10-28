# Generated by Django 3.0.8 on 2020-10-26 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(blank=True, max_length=50)),
                ('is_active', models.BooleanField(default=1)),
                ('min_amt', models.FloatField(blank=True, null=True)),
                ('percentage', models.IntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.FloatField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('receipt', models.CharField(max_length=5000)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
