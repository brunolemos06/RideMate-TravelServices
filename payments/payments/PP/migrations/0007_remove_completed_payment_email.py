# Generated by Django 4.1.7 on 2023-03-08 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PP', '0006_completed_payment_payer_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completed_payment',
            name='email',
        ),
    ]
