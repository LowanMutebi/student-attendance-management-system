# Generated by Django 5.0.6 on 2024-07-04 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_customuser_smiddlename_sharedreport'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SharedReport',
        ),
    ]
