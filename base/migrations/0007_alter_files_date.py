# Generated by Django 4.1.7 on 2023-06-01 23:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_files_date_alter_files_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 6, 1, 23, 26, 52, 314348, tzinfo=datetime.timezone.utc)),
        ),
    ]