# Generated by Django 3.1.3 on 2021-08-18 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('konsultasi', '0011_konsultasi_chat'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='konsultasi_chat',
            new_name='chat',
        ),
    ]