# Generated by Django 4.0.4 on 2022-06-01 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_alter_booking_email_alter_booking_event_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]