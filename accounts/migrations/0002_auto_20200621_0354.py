# Generated by Django 3.0.4 on 2020-06-21 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='MediaFiles',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]