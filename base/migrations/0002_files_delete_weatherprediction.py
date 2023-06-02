# Generated by Django 4.1.7 on 2023-06-01 13:18

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'ppt', 'word', 'excel'])])),
                ('date', models.DateField(default=datetime.datetime(2023, 6, 1, 13, 18, 7, 198410, tzinfo=datetime.timezone.utc))),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='WeatherPrediction',
        ),
    ]
