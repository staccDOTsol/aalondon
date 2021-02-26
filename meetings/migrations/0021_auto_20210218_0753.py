# Generated by Django 2.2.18 on 2021-02-18 07:53

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0020_auto_20210217_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='conference_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='online_link',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=100, populate_from=['title', 'postcode', 'time']),
        ),
    ]
