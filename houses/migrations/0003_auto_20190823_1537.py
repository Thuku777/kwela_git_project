# Generated by Django 2.1.5 on 2019-08-23 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_auto_20190823_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedroom',
            name='number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]