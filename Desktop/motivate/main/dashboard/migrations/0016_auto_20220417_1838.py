# Generated by Django 3.2.11 on 2022-04-17 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_remove_customer_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='firstName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='surname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
