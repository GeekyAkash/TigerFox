# Generated by Django 3.2.6 on 2021-08-29 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='ccontact_us_name',
            new_name='ccontact_name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='contact_us_date',
            new_name='contact_date',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='contact_us_email',
            new_name='contact_email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='contact_us_message',
            new_name='contact_message',
        ),
    ]