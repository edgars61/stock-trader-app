# Generated by Django 3.1.2 on 2020-10-13 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0004_auto_20201012_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pf_value_daily',
            name='date_ending',
            field=models.DateField(),
        ),
    ]