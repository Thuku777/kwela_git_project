# Generated by Django 2.1.5 on 2019-02-14 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_logo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_header', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_page', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_footer', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photoi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_logo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_header', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_footer', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]