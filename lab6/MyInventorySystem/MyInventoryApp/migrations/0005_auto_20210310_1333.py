# Generated by Django 3.1.6 on 2021-03-10 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyInventoryApp', '0004_auto_20210310_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySupplier',
            fields=[
                ('supplier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MyInventoryApp.supplier')),
            ],
            bases=('MyInventoryApp.supplier',),
        ),
        migrations.AlterField(
            model_name='waterbottle',
            name='SKU',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
