# Generated by Django 4.2.1 on 2023-05-24 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='userName',
            new_name='username',
        ),
    ]