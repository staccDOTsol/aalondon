# Generated by Django 2.2.16 on 2020-11-14 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0015_auto_20201025_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='intergroup_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
