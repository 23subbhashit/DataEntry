# Generated by Django 3.0.7 on 2021-01-11 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0005_fund_details'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='geo_tagging',
            options={'permissions': (('view_records', 'Can view records'),)},
        ),
    ]
