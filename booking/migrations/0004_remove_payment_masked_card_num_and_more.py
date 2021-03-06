# Generated by Django 4.0.4 on 2022-05-31 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_remove_booking_ticket_id_booking_event_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='masked_card_num',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='retrieval_ref_num',
        ),
        migrations.AddField(
            model_name='payment',
            name='card_number',
            field=models.CharField(default='2023-01-01', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='cvc',
            field=models.IntegerField(default=999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='exp_date',
            field=models.DateField(default='2023-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='name_of_card_holder',
            field=models.CharField(default='John Doe', max_length=200),
            preserve_default=False,
        ),
    ]
