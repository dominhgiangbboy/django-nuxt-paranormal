# Generated by Django 3.1.7 on 2021-04-02 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processApp', '0012_process_is_calculate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='付加価値額',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='process',
            name='実行予算金額',
            field=models.IntegerField(default=0),
        ),
    ]
