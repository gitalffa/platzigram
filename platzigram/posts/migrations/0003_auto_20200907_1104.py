# Generated by Django 3.0.6 on 2020-09-07 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_user_id_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id_admin',
            new_name='is_admin',
        ),
    ]