# Generated by Django 5.1 on 2024-08-14 12:39

import phone_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=phone_field.models.PhoneField(max_length=31),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='teligram_no',
            field=phone_field.models.PhoneField(max_length=31),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='whatsapp_no',
            field=phone_field.models.PhoneField(max_length=31),
        ),
    ]
