# Generated by Django 3.2.16 on 2023-08-28 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0035_alter_meeting_note_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='email_confirmed',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
