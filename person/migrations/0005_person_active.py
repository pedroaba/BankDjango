# Generated by Django 3.2.7 on 2021-10-11 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20211005_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]