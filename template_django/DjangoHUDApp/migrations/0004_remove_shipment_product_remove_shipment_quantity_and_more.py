# Generated by Django 5.0.1 on 2024-02-29 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoHUDApp', '0003_alter_shipment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='product',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='quantity',
        ),
        migrations.CreateModel(
            name='ShipmentItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjangoHUDApp.product')),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipment_items', to='DjangoHUDApp.shipment')),
            ],
        ),
    ]