# Generated by Django 2.1.7 on 2019-06-25 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20190625_1104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='_otp_secret_key',
            new_name='otp_secret_key',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='_private_key',
            new_name='private_key',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='_public_key',
            new_name='public_key',
        ),
    ]