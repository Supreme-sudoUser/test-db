# Generated by Django 3.2.11 on 2022-04-17 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_payment_paymentmethod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='paymentMethod',
        ),
    ]
