# Generated by Django 2.1.5 on 2019-08-27 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20190827_0727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property_payment',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='property_payment',
            name='property_bought',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='total_payments_expected',
            new_name='total_payments',
        ),
        migrations.RemoveField(
            model_name='account',
            name='Buyer',
        ),
        migrations.RemoveField(
            model_name='account',
            name='all_Propertys_owned',
        ),
        migrations.RemoveField(
            model_name='account',
            name='propertys_payments_made',
        ),
        migrations.AddField(
            model_name='account',
            name='buyer',
            field=models.ManyToManyField(help_text='Select The Buyer', to='accounts.Buyer'),
        ),
        migrations.AddField(
            model_name='account',
            name='deposit_paid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='payment_expected',
            field=models.IntegerField(help_text='total payment expected from all properties bought', null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='payment_made',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='property_bought',
            field=models.ManyToManyField(help_text='Select your properties', to='accounts.Property_id'),
        ),
        migrations.DeleteModel(
            name='Property_payment',
        ),
    ]
