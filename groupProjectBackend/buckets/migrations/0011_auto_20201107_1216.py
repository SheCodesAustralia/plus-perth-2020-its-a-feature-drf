# Generated by Django 3.0.8 on 2020-11-07 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buckets', '0010_auto_20201107_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='bucket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='buckets.Bucket'),
        ),
    ]
