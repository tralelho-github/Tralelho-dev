# Generated by Django 3.1.4 on 2021-01-22 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0005_auto_20210122_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countries',
            name='Translated',
        ),
        migrations.AddField(
            model_name='language',
            name='Translated',
            field=models.BooleanField(default=False),
        ),
    ]
