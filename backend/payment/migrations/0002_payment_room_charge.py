# Generated by Django 4.0.3 on 2022-03-10 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='room_charge',
            field=models.FloatField(default=0.0),
        ),
    ]