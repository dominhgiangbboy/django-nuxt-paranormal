# Generated by Django 3.1.7 on 2021-05-13 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processApp', '0003_data_set_linkfolder'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyzed_data',
            name='dataSetID',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='analyzed_data',
            name='typeID',
            field=models.IntegerField(default=1),
        ),
    ]
