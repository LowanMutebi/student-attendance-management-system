# Generated by Django 4.2.5 on 2024-06-02 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0002_courseunit_lecturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseunit',
            name='lecturer',
            field=models.ForeignKey(limit_choices_to={'is_lecturer': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course_units', to=settings.AUTH_USER_MODEL),
        ),
    ]
