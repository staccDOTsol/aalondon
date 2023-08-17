# Generated by Django 3.2.16 on 2023-08-17 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0031_alter_meeting_temporary_changes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='temporary_changes',
            field=models.TextField(blank=True, help_text='e.g. Please note that this meeting is closed on this day.', max_length=1000, null=True),
        ),
    ]
