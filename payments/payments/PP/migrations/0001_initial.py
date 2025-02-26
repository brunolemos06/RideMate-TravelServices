# Generated by Django 4.1.7 on 2023-03-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='completed_payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('payer_id', models.CharField(max_length=256)),
                ('payer_fname', models.CharField(max_length=256)),
                ('payer_lname', models.CharField(max_length=256)),
                ('amount', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ongoing_payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pp_id', models.CharField(max_length=36)),
                ('ref_id', models.CharField(max_length=256)),
                ('amount', models.CharField(max_length=256)),
            ],
        ),
    ]
