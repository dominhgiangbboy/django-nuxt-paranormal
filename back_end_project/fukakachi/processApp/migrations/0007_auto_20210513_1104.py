# Generated by Django 3.1.7 on 2021-05-13 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processApp', '0006_analyzed_data_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyzed_data',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
