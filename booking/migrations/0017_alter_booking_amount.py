# Generated by Django 4.0.4 on 2022-06-02 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_alter_booking_event_id_alter_booking_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
