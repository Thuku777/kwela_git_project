# Generated by Django 2.1.5 on 2019-02-15 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_auto_20190215_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='kwela',
            field=models.ImageField(blank=True, upload_to='kwela_pics'),
        ),
    ]