# Generated by Django 2.1.5 on 2019-08-26 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190826_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]