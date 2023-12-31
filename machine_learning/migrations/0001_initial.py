# Generated by Django 4.2.5 on 2023-09-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerChurn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=5)),
                ('account_length', models.IntegerField()),
                ('area_code', models.IntegerField()),
                ('phone_number', models.CharField()),
                ('international_plan', models.CharField(max_length=4)),
                ('voice_mail_plan', models.CharField(max_length=4)),
                ('number_vmail_messages', models.IntegerField()),
                ('total_day_minutes', models.FloatField()),
                ('total_day_calls', models.IntegerField()),
                ('total_day_charge', models.FloatField()),
                ('total_eve_minutes', models.FloatField()),
                ('total_eve_calls', models.IntegerField()),
                ('total_eve_charge', models.FloatField()),
                ('total_night_minutes', models.FloatField()),
                ('total_night_calls', models.IntegerField()),
                ('total_night_charge', models.FloatField()),
                ('total_intl_minutes', models.FloatField()),
                ('total_intl_calls', models.IntegerField()),
                ('total_intl_charge', models.FloatField()),
                ('customer_service_calls', models.IntegerField()),
                ('churn', models.BooleanField()),
            ],
        ),
    ]
