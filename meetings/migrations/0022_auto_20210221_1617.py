# Generated by Django 2.2.18 on 2021-02-21 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0021_auto_20210218_0753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='day',
        ),
        migrations.AlterField(
            model_name='meeting',
            name='postcode',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
    ]
