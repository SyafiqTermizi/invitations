# Generated by Django 2.1.1 on 2018-09-08 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0002_auto_20180908_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='email_address',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]