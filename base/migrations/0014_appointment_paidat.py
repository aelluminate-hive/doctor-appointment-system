# Generated by Django 5.1 on 2024-10-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_appointment_ispaid_appointment_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='paidAt',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]