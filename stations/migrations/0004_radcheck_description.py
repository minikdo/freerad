# Generated by Django 2.2.5 on 2019-09-07 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0003_auto_20190907_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='radcheck',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
