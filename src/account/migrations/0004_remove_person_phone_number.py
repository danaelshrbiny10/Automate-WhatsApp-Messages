# Generated by Django 4.2.2 on 2023-07-13 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_person_delete_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='phone_number',
        ),
    ]
