# Generated by Django 5.0.2 on 2024-04-10 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoHUDApp', '0011_recipient_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='batch_number',
            field=models.CharField(default='KAMIA EPILOGH', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='unit_of_measurement',
            field=models.CharField(choices=[('ΤΕΜΑΧΙΑ', 'ΤΕΜΑΧΙΑ'), ('ΜΕΤΡΑ', 'ΜΕΤΡΑ'), ('ΚΑΜΙΑ ΕΠΙΛΟΓΗ', 'ΚΑΜΙΑ ΕΠΙΛΟΓΗ')], default='ΚΑΜΙΑ ΕΠΙΛΟΓΗ', max_length=30),
        ),
    ]
