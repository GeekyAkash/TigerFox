# Generated by Django 3.2.6 on 2021-08-29 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_company_name', models.CharField(max_length=200)),
                ('client_address', models.CharField(max_length=800)),
                ('client_email', models.EmailField(max_length=200)),
                ('client_phone', models.IntegerField()),
                ('client_massage', models.TextField()),
                ('client_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccontact_us_name', models.CharField(max_length=100)),
                ('contact_us_email', models.EmailField(max_length=150)),
                ('contact_us_message', models.TextField()),
                ('contact_us_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=100)),
                ('supplier_company_name', models.CharField(max_length=150)),
                ('supplier_address', models.CharField(max_length=800)),
                ('supplier_email', models.EmailField(max_length=200)),
                ('supplier_phone', models.IntegerField()),
                ('supplier_message', models.TextField()),
                ('supplier_date', models.DateField()),
            ],
        ),
    ]
