# Generated by Django 4.2.5 on 2024-06-21 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='Staff_ID',
            field=models.CharField(default='L/COCIS/MUK/001', max_length=15),
        ),
    ]
