# Generated by Django 2.2.7 on 2019-12-17 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20191217_0937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='checkin',
            new_name='check',
        ),
    ]
