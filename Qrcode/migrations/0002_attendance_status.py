# Generated by Django 4.2.5 on 2024-06-30 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Qrcode', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('present', 'Present'), ('absent', 'Absent')], default='absent', max_length=7),
        ),
    ]
