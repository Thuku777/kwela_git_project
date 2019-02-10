# Generated by Django 2.1.5 on 2019-01-18 16:03

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('identity_number', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='e.g property history, ownership, development')),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('is_BMVP', models.BooleanField(default=False)),
                ('Registration_date', models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='Date when buyer registered')),
                ('Deposit_date', models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='Date when buyer paid deposit')),
                ('installment_date', models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='Date when buyer payed installment')),
                ('Buying_date', models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='Date when buyer bought the property or finished paying for the property')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a Location (e.g. Ruiru, Mwea, e.t.c)', max_length=200)),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='define how many plots are what size, area history')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('identity_number', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='e.g property history, ownership, development')),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('is_published', models.BooleanField(default=False)),
                ('Registration_date', models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='Date when buyer registered')),
                ('listingAgreement_date', models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='Date when buyer registered')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Paymenttype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the type of payment choosen by the client (e.g. Cash, 3 months installments, 6 months installments e.t.c)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', ckeditor.fields.RichTextField(help_text='Enter a brief description of the property ownership', max_length=1000)),
                ('Paymenttype', models.ManyToManyField(help_text='select payment method', to='catalog.Paymenttype')),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Buyer')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Listing')),
                ('location', models.ManyToManyField(help_text='select location', to='catalog.Location')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole system', primary_key=True, serialize=False)),
                ('price', models.CharField(max_length=200)),
                ('paymentdue_when', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('s', 'Sold'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='a', help_text='Plot availability', max_length=1)),
                ('debtor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Property')),
            ],
        ),
        migrations.CreateModel(
            name='Propertytype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the type of plot (e.g. Commercial Plot, Rent house, e.t.c)', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='propertytype',
            field=models.ManyToManyField(help_text='select property type', to='catalog.Propertytype'),
        ),
        migrations.AddField(
            model_name='buyer',
            name='owner',
            field=models.ForeignKey(help_text='Owner Assigned', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Owner'),
        ),
    ]