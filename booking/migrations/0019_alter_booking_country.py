# Generated by Django 4.0.4 on 2022-06-02 19:24

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0018_delete_payment_booking_date_booking_subtotal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
