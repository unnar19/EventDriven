# Generated by Django 4.0.4 on 2022-06-02 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_remove_payment_card_number_remove_payment_cvc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='booking_id',
        ),
    ]