# Generated by Django 3.2.11 on 2022-04-11 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_rename_initialpayment_payment_actual_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='Actual_payment',
        ),
        migrations.AddField(
            model_name='purchase',
            name='actual_payment',
            field=models.IntegerField(null=True),
        ),
    ]
