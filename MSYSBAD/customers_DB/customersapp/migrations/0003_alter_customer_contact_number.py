# Generated by Django 3.2.2 on 2022-02-28 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customersapp', '0002_auto_20220228_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='contact_number',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
