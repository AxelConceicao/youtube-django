# Generated by Django 3.1.5 on 2021-04-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20210427_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Views count'),
        ),
    ]
