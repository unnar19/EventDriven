# Generated by Django 4.0.4 on 2022-06-01 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_alter_booking_house_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='zip',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.CharField(max_length=256),
        ),
    ]
