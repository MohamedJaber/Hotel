# Generated by Django 2.2.7 on 2019-12-17 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_auto_20191217_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='guest',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.guest'),
        ),
    ]
