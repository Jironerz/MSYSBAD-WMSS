# Generated by Django 3.2.2 on 2022-02-28 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customersapp', '0003_alter_customer_contact_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Account',
        ),
    ]
