# Generated by Django 3.2.11 on 2022-04-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_property_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
