# Generated by Django 3.0.7 on 2021-07-04 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0020_auto_20210703_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='description',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]
