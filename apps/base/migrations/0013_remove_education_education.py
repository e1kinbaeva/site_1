# Generated by Django 5.0.6 on 2024-06-06 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_education_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='education',
        ),
    ]
