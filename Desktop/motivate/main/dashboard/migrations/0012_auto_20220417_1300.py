# Generated by Django 3.2.11 on 2022-04-17 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20220413_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='firstName',
            new_name='fullName',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='surname',
        ),
    ]
