# Generated by Django 2.2.19 on 2021-03-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0022_auto_20210221_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('organisation', models.CharField(max_length=200)),
                ('email', models.EmailField(default='doesnotexist@aalondon.com', max_length=254)),
                ('update_to_gso', models.BooleanField(default=False)),
            ],
        ),
    ]