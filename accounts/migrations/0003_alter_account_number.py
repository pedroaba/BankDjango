# Generated by Django 3.2.7 on 2021-10-06 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_translations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='number',
            field=models.CharField(auto_created=True, max_length=10, unique=True),
        ),
    ]