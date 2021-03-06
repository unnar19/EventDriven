# Generated by Django 4.0.4 on 2022-05-24 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('address', models.CharField(max_length=150)),
                ('zip', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('subtotal', models.IntegerField()),
                ('masked_card_num', models.CharField(max_length=200)),
                ('retrieval_ref_num', models.CharField(max_length=200)),
            ],
        ),
    ]
