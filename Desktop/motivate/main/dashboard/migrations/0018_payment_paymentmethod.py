# Generated by Django 3.2.11 on 2022-04-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_auto_20220417_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='paymentMethod',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
