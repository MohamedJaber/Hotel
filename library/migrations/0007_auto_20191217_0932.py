# Generated by Django 2.2.7 on 2019-12-17 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20191214_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='name',
            new_name='username',
        ),
    ]
